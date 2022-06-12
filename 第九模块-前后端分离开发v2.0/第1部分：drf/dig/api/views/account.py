import uuid
import datetime
from django.db.models import Q
from django.urls import reverse

from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from api.extension.mixins import DigCreateModelMixin
from api.serializers.account import RegisterSerializer, AuthSerializer
from api.extension import return_code
from api import models

from rest_framework.mixins import CreateModelMixin

"""
1. 只需要提供POST方法
2. 请求进来执行 DigCreateModelMixin的create方法
3. 获取数据request.data，进行校验（RegisterSerializer）
"""


class RegisterView(DigCreateModelMixin, GenericViewSet):
    """ 用户注册 """

    authentication_classes = []
    permission_classes = []
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        serializer.validated_data.pop('confirm_password')
        # super().perform_create(serializer)
        serializer.save()


class AuthView(APIView):
    """ 用户登录 """
    authentication_classes = []
    permission_classes = []

    # 2. 数据库校验用户名和密码的合法性
    def post(self, request):
        # 1. 获取用户请求 & 校验
        serializer = AuthSerializer(data=request.data)
        if not serializer.is_valid():
            # { 'username':[错误信息,], 'phone':[xxxx,]}
            return Response({"code": return_code.VALIDATE_ERROR, 'detail': serializer.errors})

        username = serializer.validated_data.get('username')
        phone = serializer.validated_data.get('phone')
        password = serializer.validated_data.get('password')

        user_object = models.UserInfo.objects.filter(Q(Q(username=username) | Q(phone=phone)),
                                                     password=password).first()

        if not user_object:
            return Response({"code": return_code.VALIDATE_ERROR, "error": "用户名或密码错误"})

        token = str(uuid.uuid4())
        user_object.token = token
        # 设置token有效期：当前时间 + 2周
        user_object.token_expiry_date = datetime.datetime.now() + datetime.timedelta(weeks=2)
        user_object.save()

        return Response({"code": return_code.SUCCESS, "data": {"token": token, "name": user_object.username}})
