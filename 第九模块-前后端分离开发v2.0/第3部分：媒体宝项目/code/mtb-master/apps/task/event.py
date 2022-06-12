import time
import datetime
import xml.etree.cElementTree as ET
from . import models
from apps.base import models as base_model
import requests
import json
from utils.token import get_authorizer_access_token
from urllib.parse import quote_plus
from django.conf import settings


def handler(authorizer_app_id, decrypt_xml):
    xml_tree = ET.fromstring(decrypt_xml)
    msg_type = xml_tree.find("MsgType").text

    if msg_type == "text":
        # 文本=关键字 & 公众号参与活动了 & 活动时间
        content = xml_tree.find("Content").text
        user_open_id = xml_tree.find("FromUserName").text

        public_object = base_model.PublicNumbers.objects.filter(authorizer_app_id=authorizer_app_id).first()
        if not public_object:
            return

        current_datetime = datetime.datetime.now()
        activity_object = models.Activity.objects.filter(
            start_time__lt=current_datetime,
            end_time__gt=current_datetime,
            poster__key=content,
            publics__public=public_object
        ).order_by('-id').first()

        if not activity_object:
            return

        rules = activity_object.poster.rules
        # 用户 & 参与活动

        # 公众号已将此粉丝拉黑
        black = models.TakePartIn.objects.filter(public_number=public_object, open_id=user_open_id, black=1).exists()
        if black:
            return

        # 已参与
        tp = models.TakePartIn.objects.filter(activity=activity_object, public_number=public_object,
                                              open_id=user_open_id).first()
        if not tp:
            tp = models.TakePartIn.objects.create(
                activity=activity_object,
                public_number=public_object,
                open_id=user_open_id
            )
        else:
            # tp.part_in # 0已参与 / 1只是助力
            if tp.part_in == 0:
                return
            tp.part_in = 0
            tp.save()

        # 给用户发送消息
        access_token = get_authorizer_access_token(public_object)
        requests.post(
            url="https://api.weixin.qq.com/cgi-bin/message/custom/send",
            params={"access_token": access_token},
            data=json.dumps({
                "touser": user_open_id,
                "msgtype": "text",
                "text": {
                    "content": rules
                }
            }, ensure_ascii=False).encode('utf-8')
        )

        # 发送图文消息（用于引导用户授权并获取昵称和头像）
        url = "https://open.weixin.qq.com/connect/oauth2/authorize?appid={}&redirect_uri={}&response_type=code&scope=snsapi_userinfo&state={}&component_appid={}#wechat_redirect"
        auth_url = url.format(authorizer_app_id, quote_plus("http://mtb.pythonav.com/api/task/oauth"), tp.pk,
                              settings.WX_APP_ID)

        requests.post(
            url="https://api.weixin.qq.com/cgi-bin/message/custom/send",
            params={"access_token": access_token},
            data=json.dumps({
                "touser": user_open_id,
                "msgtype": "news",
                "news": {
                    "articles": [
                        {
                            "title": "点击链接生成我的专属海报",
                            "description": "邀请好友助力即可领取奖励",
                            "url": auth_url,
                            "picurl": ""
                        }
                    ]
                }
            }, ensure_ascii=False).encode('utf-8')
        )

    if msg_type == "event":
        event = xml_tree.find("Event").text
        event_key = xml_tree.find("EventKey").text  # qrscene_1_1

        if event == "subscribe":
            from_use_open_id = xml_tree.find("FromUserName").text
            pub_object = base_model.PublicNumbers.objects.filter(authorizer_app_id=authorizer_app_id).first()
            models.TakePartIn.objects.filter(open_id=from_use_open_id, public_number=pub_object).update(looking=0,
                                                                                                        subscribe_time=datetime.datetime.now())

        if event == "subscribe" and event_key and event_key.startswith("qrscene_1_"):
            # 助力

            # 给谁助力？
            tp_id = event_key.rsplit("_", maxsplit=1)[-1]
            tp_object = models.TakePartIn.objects.filter(id=tp_id).first()

            # 任务有效期
            ctime = datetime.datetime.now()
            if ctime < tp_object.activity.start_time or ctime > tp_object.activity.end_time:
                return

            # 助力者是否还可以助力 & 是否被拉黑
            from_use_open_id = xml_tree.find("FromUserName").text

            # 1.检查活动是否是拉新，如果是，则只能新关注的人才行。
            # 1.1 开启拉新保护，只有新用户助力才行
            if tp_object.activity.protect_switch:
                is_old_fans = models.TakePartIn.objects.filter(open_id=from_use_open_id).exists()
                if is_old_fans:
                    return

            # 1.2 关闭新保护，新老用户都可以助力（只要未给这个活动助力过就行）
            else:
                has_help = models.TakePartIn.objects.filter(open_id=from_use_open_id,
                                                            activity=tp_object.activity).exists()
                if has_help:
                    return

            # 2.检查此人是否被拉黑（公众号级别）
            black = models.TakePartIn.objects.filter(open_id=from_use_open_id, public_number=tp_object.public_number,
                                                     black=1).exists()
            if black:
                return

            # 3.正常参与助力
            models.TakePartIn.objects.create(
                activity=tp_object.activity,
                public_number=tp_object.public_number,
                open_id=from_use_open_id,
                origin=0,  # 其他粉丝
                part_in=1,  # 不参与，只助力（是否可以参与活动？）
                level=tp_object.level + 1,
                origin_open_id=tp_object.open_id,  # 帮助的那个人的 user_open_id
                subscribe_time=datetime.datetime.now()
            )

            # 4.参与者：数量+1 + 任务级别
            tp_object.number += 1
            level_queryset = models.Award.objects.filter(activity=tp_object.activity_object).order_by("-count")
            for item in level_queryset:
                if tp_object.number >= item.count:
                    tp_object.task_progress = item.level
                    continue
            tp_object.save()



            # 5.给要助力的人发送客服消息（新有一个人帮你助力了，现在已有多少人）
            access_token = get_authorizer_access_token(tp_object.public_number)
            requests.post(
                url="https://api.weixin.qq.com/cgi-bin/message/custom/send",
                params={"access_token": access_token},
                data=json.dumps({
                    "touser": tp_object.open_id,
                    "msgtype": "text",
                    "text": {
                        "content": "您的朋友帮你助力成功，目前已助力{}人".format(tp_object.number)
                    }
                }, ensure_ascii=False).encode('utf-8')
            )

        if event == "subscribe" and event_key and event_key.startswith("qrscene_2_"):
            user_open_id = xml_tree.find("FromUserName").text
            promo_id = event_key.rsplit("_", maxsplit=1)[-1]
            # 推广码过来的粉丝（只记录，不考虑参加活动，他可以再发关键字参与活动）

            # 公众号对象
            pub_object = base_model.PublicNumbers.objects.filter(authorizer_app_id=authorizer_app_id).first()

            # 是否已是粉丝（如果是老粉丝就不记录，解决取关再关注的问题）
            is_fans = models.TakePartIn.objects.filter(open_id=user_open_id, public_number=pub_object).exists()
            if is_fans:
                return

            # 新增粉丝记录（未参与任何活动）
            models.TakePartIn.objects.create(
                # activity=tp_object.activity
                public_number=pub_object,
                open_id=user_open_id,
                origin=1,  # 推广码
                part_in=1,  # 不参与
                origin_open_id=promo_id,  # 推广码ID
                subscribe_time=datetime.datetime.now()
            )

        if event == "unsubscribe":
            pub_object = base_model.PublicNumbers.objects.filter(authorizer_app_id=authorizer_app_id).first()
            if not pub_object:
                return
            from_use_open_id = xml_tree.find("FromUserName").text
            models.TakePartIn.objects.filter(open_id=from_use_open_id, public_number=pub_object).update(looking=1)
