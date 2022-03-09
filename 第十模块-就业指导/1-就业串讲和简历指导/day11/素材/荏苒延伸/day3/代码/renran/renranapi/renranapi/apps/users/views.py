# Create your views here.
from rest_framework.views import APIView
from django.conf import settings
import json
from urllib.parse import urlencode
from urllib.request import urlopen
from rest_framework.response import Response
from rest_framework import status

class CaptchaAPIView(APIView):
    def get(self,request):
        """验证码的验证结果校验"""
        AppSecretKey = settings.TENCENT_CAPTCHA["App_Secret_Key"]
        appid = settings.TENCENT_CAPTCHA["APPID"]
        Ticket = request.query_params.get("ticket")
        Randstr = request.query_params.get("randstr")
        UserIP = request._request.META.get("REMOTE_ADDR")
        print("用户ID地址：%s" % UserIP)
        params = {
            "aid": appid,
            "AppSecretKey": AppSecretKey,
            "Ticket": Ticket,
            "Randstr": Randstr,
            "UserIP": UserIP
        }
        params = urlencode(params)

        f = urlopen("%s?%s" % (settings.TENCENT_CAPTCHA["GATEWAY"], params))
        content = f.read()
        res = json.loads(content)
        print(res)
        if res:
            error_code = res["response"]
            if error_code == "1":
                return Response("验证通过！")
            else:
                return Response("验证失败！%s" % res["err_msg"], status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("验证失败！", status=status.HTTP_400_BAD_REQUEST)

from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import UserModelSerializer
class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

import random
from django_redis import get_redis_connection
from renranapi.settings import constants
from mycelery.sms.tasks import send_sms

class SMSCodeAPIView(APIView):
    """
    短信验证码
    """
    def get(self, request, mobile):
        """
        短信验证码
        """
        redis_conn = get_redis_connection('sms_code')

        # 手机号是否处于发送短信的冷却时间内
        interval = redis_conn.get("sms_time_%s" % mobile)
        if interval is not None:
            return Response("不能频繁发送短信！")

        # 生成短信验证码
        sms_code = "%06d" % random.randint(0, 999999)

        # 保存短信验证码与发送记录
        # 使用redis提供的管道操作可以一次性执行多条redis命令
        pl = redis_conn.pipeline()
        pl.multi()
        pl.setex("sms_%s" % mobile, constants.SMS_CODE_EXPIRE, sms_code)      # 设置短信有效期
        pl.setex("sms_time_%s" % mobile, constants.SMS_CODE_INTERVAL, "_")    # 设置发送短信间隔为60s
        pl.execute()

        # 发送短信验证码
        send_sms.delay(mobile, sms_code)

        return Response({"message": "OK"}, status.HTTP_200_OK)

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadData
from mycelery.email.tasks import send_email
class ResetPasswordAPIView(APIView):
    def get(self,request):
        """发送找回密码的链接地址"""

        # 检测用户是否存在
        email = request.query_params.get("email")
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response("当前邮箱对应的用户不存在！", status=status.HTTP_400_BAD_REQUEST)

        # 生成找回密码的链接
        serializer = Serializer(settings.SECRET_KEY, constants.DATA_SIGNATURE_EXPIRE)
        # dumps的返回值是加密书的bytes信息
        access_token = serializer.dumps({"email":email}).decode()

        url = settings.CLIENT_HOST+"/reset_password?access_token="+access_token

        # 使用dango提供的email发送邮件
        send_email.delay([email],url)

        return Response("邮件已经发送，请留意您的邮箱")

    def post(self,request):
        # 验证邮箱链接地址中的access_token是否正确并在有效期时间范围内
        access_token = request.data.get("access_token")
        serializer = Serializer(settings.SECRET_KEY, constants.DATA_SIGNATURE_EXPIRE)
        try:
            data = serializer.loads(access_token)
            return Response({"email": data.get("email")})
        except BadData:
            # access_token过期或者错误
            return Response("重置密码的邮件已过期或者邮件地址有误！", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        # 重置密码
        # 再次从access_token获取用户信息
        access_token = request.data.get("access_token")
        password = request.data.get("password")
        password2 = request.data.get("password2")

        # 判断密码和确认密码是否一致
        if len(password) < 6 or len(password) > 16:
            return Response("密码长度有误！", status=status.HTTP_400_BAD_REQUEST)

        if password != password2:
            return Response("密码和确认密码不一致！", status=status.HTTP_400_BAD_REQUEST)

        serializer = Serializer(settings.SECRET_KEY, constants.DATA_SIGNATURE_EXPIRE)
        try:
            data = serializer.loads(access_token)
        except BadData:
            # access_token过期或者错误
            return Response("重置密码的邮件已过期或者邮件地址有误！", status=status.HTTP_400_BAD_REQUEST)

        email = data.get('email')
        # 获取用户信息
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response("重置密码失败！邮箱地址有误！", status=status.HTTP_400_BAD_REQUEST)

        # 修改密码
        user.set_password(password)
        user.save()

        return Response("重置密码成功！")


from tablestore import *
from rest_framework.permissions import IsAuthenticated
from datetime import datetime

class FollowAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @property
    def client(self):
        return OTSClient(settings.OTS_ENDPOINT, settings.OTS_ID, settings.OTS_SECRET, settings.OTS_INSTANCE)

    def post(self,request):
        """粉丝关注作者"""
        follow = request.user # 粉丝ID
        author_id = request.data.get("author_id") # 获取作者ID

        table_name = "user_relation_table"
        # 主键列
        primary_key = [('user_id', author_id), ('follow_user_id',follow.id)]
        attribute_columns = [('timestamp', datetime.now().timestamp())]
        row = Row(primary_key, attribute_columns)
        self.client.put_row(table_name, row)

        return Response({"message":"关注成功!"})

    def delete(self,request):
        """粉丝取关作者"""
        follow = request.user # 粉丝ID
        author_id = int(request.query_params.get("author_id")) # 获取作者ID
        table_name = "user_relation_table"
        # 主键列
        primary_key = [('user_id', author_id), ('follow_user_id',follow.id)]
        row = Row(primary_key)
        consumed, return_row = self.client.delete_row(table_name, row, None)
        return Response({"message": "取消关注成功!"})


from .models import User
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
class UserCenterAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    # 设置当前用户访问自己的数据
    def get(self,request,pk):
        user = request.user
        if user.id !=int(pk):
            return Response({"message":"对不起，您无权访问其他用户信息"}, status=status.HTTP_403_FORBIDDEN)

        return Response({
            "money": request.user.money,
        })

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import RecordModelSerializer
from .models import Record
class UserRecordAPIView(ListAPIView):
    """收支记录"""
    serializer_class = RecordModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Record.objects.filter(user=user)
        return queryset

from rest_framework.permissions import IsAuthenticated
from .models import Message
from renranapi.utils.helpers import message_sort
class UserMessageAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        """读取其他用户给当前用户的鱼书信息"""
        recevie = request.user # 当前登录用户属于接收者
        redis_conn = get_redis_connection("message")
        message_list = redis_conn.keys("message_%s_*" % recevie.id)

        # 对信息的键进行排序
        message_list = message_sort(message_list)

        # 从message_list进行遍历到redis提取信息
        data_list = []
        for key in message_list:
            key_data = key.decode().split("_")
            message = redis_conn.hgetall(key)

            # 因为这里是属于信息列表，所以我们需要查询已经阅读的数据
            if int(message["status".encode()]) == 0:
                # 判断: 信息的发送者是否已经添加到data_list
                # 如果在，则我们直接在列表data_list的字典成员的message_list追加一个信息
                # 如果不在，则我们直接在列表data_list中新增一个当前发送者的字典成员
                # key_data[1] # 发送者
                if len(data_list)<1:
                    data_list.append({
                        "sender": message["sender".encode()], #　发送者昵称
                        "sender_id": key_data[2],             # 发送者id
                        "sender_avatar": message["avatar".encode()], # 发送者头像
                        "last_time": key_data[-1][:4] + "-" + key_data[-1][4:6] + "-" + key_data[-1][6:8] + " " +
                                        key_data[-1][8:10] + ":" + key_data[-1][10:12] + ":" + key_data[-1][12:14],             # 信息发送的最后时间
                        "message_list":[
                            {
                                "message":message["message".encode()].decode(),
                                "status": message["status".encode()].decode(),
                                "time": key_data[-1][:4] + "-" + key_data[-1][4:6] + "-" + key_data[-1][6:8] + " " +
                                        key_data[-1][8:10] + ":" + key_data[-1][10:12] + ":" + key_data[-1][12:14],

                            }
                        ],
                    })
                else:
                    for item in data_list:
                        print(item["sender_id"])
                        print(key_data[2])
                        if item["sender_id"] == key_data[2]:
                            recevie = item
                            break
                        else:
                            recevie = False

                    if recevie:
                        # 在原有字典中的message里面追加信息
                        recevie["last_time"] = key_data[-1][:4] + "-" + key_data[-1][4:6] + "-" + key_data[-1][6:8] + " " + key_data[-1][8:10] + ":" + key_data[-1][10:12] + ":" + key_data[-1][12:14]
                        recevie["message_list"].append({
                            "message": message["message".encode()].decode(),
                            "status": message["status".encode()].decode(),
                            "time": key_data[-1][:4]+"-"+key_data[-1][4:6]+"-"+key_data[-1][6:8]+" "+ key_data[-1][8:10]+":"+key_data[-1][10:12]+":"+key_data[-1][12:14],

                        })
                    else:
                        # 在data_list里面追加字典成员
                        data_list.append({
                            "sender": message["sender".encode()],  # 发送者昵称
                            "sender_id": key_data[2],  # 发送者id
                            "sender_avatar": message["avatar".encode()], # 发送者头像
                            "last_time": key_data[-1][:4] + "-" + key_data[-1][4:6] + "-" + key_data[-1][6:8] + " " +key_data[-1][8:10] + ":" + key_data[-1][10:12] + ":" + key_data[-1][12:14],  # 信息发送的最后时间
                            "message_list": [
                                {
                                    "message": message["message".encode()].decode(),
                                    "status": message["status".encode()].decode(),
                                    "time": key_data[-1][:4]+"-"+key_data[-1][4:6]+"-"+key_data[-1][6:8]+" "+ key_data[-1][8:10]+":"+key_data[-1][10:12]+":"+key_data[-1][12:14],
                                }
                            ],
                        })
        """
        # 把得到的数据进行重构，形成列表，列表里面每一个成员就是当前用户接收来自不同用户的信息
        data_list = [
            {
                "last_time": 最后发送信息的时间,[第一排序条件]
                "sender_id": 发送者信息,
                "sender": 发送者信息,
                "sender_avatar": 发送者信息,
                "message_list":[
                    {"message":"内容","created_time":发送时间,"status": "0",},[时间排序]
                    {"message":"内容","created_time":发送时间,"status": "0",},
                    {"message":"内容","created_time":发送时间,"status": "0",},
                ] 
            }
        ]
        """
        return Response(data_list)

    def post(self,request):
        """发送当前用户的鱼书信息给其他用户"""
        # 获取发送者的用户信息
        sender = request.user # 当前登录用户属于发送者
        message = request.data.get("message"," ")
        recevie = request.data.get("recevie")

        # 验证数据[作业：去除把信息的两边空格去掉]
        message2 = message.strip()
        if len(message2) < 1:
            return Response({"message":"不能发送空信息！"})

        try:
            User.objects.get( pk=recevie )
        except User.DoesNotExist:
            return Response({"message":"对方用户不存在！"})

        redis_conn = get_redis_connection("message")
        """
        保存数据的格式：
        message_<recevie_id>_<sender_id>_<time>:{
            sender: "",  // 发送者昵称
            message:"",
            status:"",
            avatar:"",   // 新增一个字段保存头像，可以减少查询数据库
        }
        """
        pipe = redis_conn.pipeline()
        pipe.multi()
        pipe.hset("message_%s_%s_%s" % (recevie, sender.id, datetime.now().strftime("%Y%m%d%H%M%S")), "message", message)
        pipe.hset("message_%s_%s_%s" % (recevie, sender.id, datetime.now().strftime("%Y%m%d%H%M%S")), "status", 0)
        pipe.hset("message_%s_%s_%s" % (recevie, sender.id, datetime.now().strftime("%Y%m%d%H%M%S")), "sender", sender.nickname)
        pipe.hset("message_%s_%s_%s" % (recevie, sender.id, datetime.now().strftime("%Y%m%d%H%M%S")), "avatar", sender.avatar.url)
        pipe.execute()

        return Response({"message":"发送信息成功！"})


from rest_framework.permissions import IsAuthenticated
class ChatMessageAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,chat_id):
        """获取双方的聊天记录"""
        # 1. 获取双方的id
        user_id = request.user.id

        # 2. 到redis里面进行查找
        redis_conn = get_redis_connection("message")
        # 2.1. 对方发给我的信息
        message_list_key_recevie = redis_conn.keys("message_%s_%s_*" % (user_id, chat_id))
        # 2.2. 我给对方的信息
        message_list_key_sender = redis_conn.keys("message_%s_%s_*" % (chat_id, user_id))
        message_list = message_list_key_recevie + message_list_key_sender

        # 3. 把所有的聊天记录按时间进行排序
        message_list = message_sort(message_list)

        # 4. 把所有聊天记录进行数据重构
        data_list = []
        for key in message_list:
            message = redis_conn.hgetall(key)
            key_data = key.decode().split("_")
            time = key_data[-1]
            data_list.append({
                "sender": message["sender".encode()].decode(),
                "message": message["message".encode()].decode(),
                "avatar": message["avatar".encode()].decode(),
                "time":   time[:4]+"-"+time[4:6]+"-"+time[6:8]+" "+ time[8:10]+":"+time[10:12]+":"+time[12:14],
            })

            # 把未读信息的状态修改成已读取状态
            if message["status".encode()].decode() == "0":
                redis_conn.hset(key, "status", 1)

        # 在redis中记录当前用户获取最后一个消息的key值
        redis_conn.set("%s_read_last_message" % user_id, key)

        return Response(data_list)


class MesageAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,chat_id):
        """获取对方发送过来的最新信息"""
        user_id = request.user.id
        redis_conn = get_redis_connection("message")
        last_key = redis_conn.get("%s_read_last_message" % user_id)
        last_time = last_key.decode().split("_")[-1]

        # 2.1. 对方发给我的信息
        message_list = redis_conn.keys("message_%s_%s_*" % (user_id, chat_id))
        message_list = message_sort(message_list)

        data_list = []
        for key in message_list:
            key_data = key.decode().split("_")
            time = key_data[-1]
            if time > last_time:
                """未读取的信息"""
                message = redis_conn.hgetall(key)

                data_list.append({
                    "sender": message["sender".encode()].decode(),
                    "message": message["message".encode()].decode(),
                    "avatar": message["avatar".encode()].decode(),
                    "time": time[:4] + "-" + time[4:6] + "-" + time[6:8] + " " + time[8:10] + ":" + time[10:12] + ":" + time[12:14],
                })

                redis_conn.hset(key, "status", 1)

        # 在redis中记录当前用户获取最后一个消息的key值
        redis_conn.set("%s_read_last_message" % user_id, key)

        return Response(data_list)