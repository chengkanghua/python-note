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