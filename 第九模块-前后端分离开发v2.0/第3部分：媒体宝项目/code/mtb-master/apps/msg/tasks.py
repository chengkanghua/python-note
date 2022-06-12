import json
import time
import requests
from celery import shared_task
from django.db.models import F
from utils.token import get_authorizer_access_token
from . import models


# @shared_task
@shared_task(ignore_result=True)
def send_service_message(message_id, authorizer_app_id):
    """ celery任务：客服消息 """

    # 1.状态更新，正在发送
    message_object = models.Message.objects.filter(id=message_id).first()
    message_object.status = 2
    message_object.save()

    # 2.获取公众号48小时内有交互的用户OpenID
    ctime = int(time.time())
    interaction_list = models.Interaction.objects.filter(authorizer_app_id=authorizer_app_id, end_date__gt=ctime)
    for obj in interaction_list:
        user_open_id = obj.user_open_id

        access_token = get_authorizer_access_token(message_object.public)
        # 3.发送文本消息
        if message_object.content:
            requests.post(
                url="https://api.weixin.qq.com/cgi-bin/message/custom/send",
                params={"access_token": access_token},
                data=json.dumps({
                    "touser": user_open_id,
                    "msgtype": "text",
                    "text": {
                        "content": message_object.content
                    }
                }, ensure_ascii=False).encode('utf-8')
            )
        # 4.发送图片信息
        if message_object.media_id:
            requests.post(
                url="https://api.weixin.qq.com/cgi-bin/message/custom/send",
                params={"access_token": access_token},
                json={
                    "touser": user_open_id,
                    "msgtype": "image",
                    "image": {
                        "media_id": message_object.media_id
                    }
                }
            )

        # 5.更新数量（100次）
        models.Message.objects.filter(id=message_id).update(count=F("count") + 1)

    # 6.更新状态
    models.Message.objects.filter(id=message_id).update(status=3)


def get_total_fans_open_id(message_object):
    next_open_id = None
    while True:
        params = {"access_token": get_authorizer_access_token(message_object.public)}
        if next_open_id:
            params['next_open_id'] = next_open_id

        data_dict = requests.get(
            url="https://api.weixin.qq.com/cgi-bin/user/get",
            params=params
        ).json()

        if not data_dict['data']['openid']:
            return

        for open_id in data_dict['data']['openid']:
            yield open_id

        if data_dict['total'] == data_dict['count']:
            return

        next_open_id = data_dict["next_openid"]


@shared_task(ignore_result=True)
def send_template_message(message_id, authorizer_app_id, item_dict):
    # 1.状态更新，正在发送
    message_object = models.Message.objects.filter(id=message_id).first()
    message_object.status = 2
    message_object.save()

    if message_object.interaction == 1:
        # 48互动
        ctime = int(time.time())
        interaction_list = models.Interaction.objects.filter(authorizer_app_id=authorizer_app_id,
                                                             end_date__gt=ctime).all()
        open_id_list = []
        for obj in interaction_list:
            open_id_list.append(obj.user_open_id)
    else:
        # 不限制(生成器）
        open_id_list = get_total_fans_open_id(message_object)

    # 2.发送消息
    for user_open_id in open_id_list:
        requests.post(
            url="https://api.weixin.qq.com/cgi-bin/message/template/send",
            params={"access_token": get_authorizer_access_token(message_object.public)},
            json={
                "touser": user_open_id,
                "template_id": message_object.template_id,
                "data": {k: {"value": v} for k, v in item_dict.items()}
            }
        )
        # print(user_open_id, res.text)
        # 3.更新数量
        models.Message.objects.filter(id=message_id).update(count=F("count") + 1)

    # 4.更新状态
    models.Message.objects.filter(id=message_id).update(status=3)


@shared_task(ignore_result=True)
def send_template_sop(message_id, authorizer_app_id, item_dict):
    # 1.状态更新，正在发送
    sop_object = models.Sop.objects.filter(id=message_id).first()
    sop_object.status = 2
    sop_object.save()

    # open_id_list = get_total_fans_open_id(sop_object)

    # 测试：
    ctime = int(time.time())
    interaction_list = models.Interaction.objects.filter(authorizer_app_id=authorizer_app_id,
                                                         end_date__gt=ctime).all()
    open_id_list = []
    for obj in interaction_list:
        open_id_list.append(obj.user_open_id)

    # 2.发送消息
    for user_open_id in open_id_list:
        requests.post(
            url="https://api.weixin.qq.com/cgi-bin/message/template/send",
            params={"access_token": get_authorizer_access_token(sop_object.public)},
            json={
                "touser": user_open_id,
                "template_id": sop_object.template_id,
                "data": {k: {"value": v} for k, v in item_dict.items()}
            }
        )
        # print(user_open_id, res.text)
        # 3.更新数量
        models.Sop.objects.filter(id=message_id).update(count=F("count") + 1)

    # 4.更新状态
    models.Sop.objects.filter(id=message_id).update(status=3)
