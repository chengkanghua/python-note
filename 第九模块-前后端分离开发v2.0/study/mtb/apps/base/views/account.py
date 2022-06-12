import jwt
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from .. import models
from ..serializers.account import AuthSerializer
from utils import return_code


class AuthView(APIView):
    # 登录页面不用验证token
    authentication_classes = []
    permission_classes = []
    def post(self, request, *args, **kwargs):
        print(request.user)
        print(request.auth)
        # 1 获取用户请求发送的用户名  弥漫

        # 2 数据校验（用户名 密码）
        serializer = AuthSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"code": return_code.FIELD_ERROR, "detail": serializer.errors})

        # 3 数据库校验 （用户名 密码）
        username = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")
        user_object = models.UserInfo.objects.filter(username=username, password=password).first()
        if not user_object:
            return Response({"code": return_code.VALIDATE_ERROR, "detail": "用户名或密码错误"})

        # 4 生成jwt token返回
        headers = {
            'typ': 'jwt',
            'alg': 'HS256'
        }
        # 构造payload
        payload = {
            'user_id': user_object.id,  # 自定义id
            'username': user_object.username,  # 自定义用户名
            'exp': datetime.datetime.now() + datetime.timedelta(days=7)  # 超时时间
        }

        token = jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm="HS256", headers=headers)

        return Response({"code": return_code.SUCCESS, "data": {"token": token, 'username': username}})


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        # print(request.user.user_id)
        # print(request.user.username)
        # print(request.user.exp)
        return Response("test")
