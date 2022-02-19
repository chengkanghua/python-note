from django.shortcuts import render
import uuid
from .models import User
from utils.auth import MyAuth
from utils.permission import MyPermission
from utils.throttle import MyThrottle
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

class DemoView(APIView):
    def get(self,request):
        return Response("认证demo")

class LoginView(APIView):
    def post(self,request):
        username =request.data.get("username")
        pwd = request.data.get("pwd")
        # 登陆成功 生成token 会吧token给你返回
        token = uuid.uuid4()
        User.objects.create(username=username,pwd=pwd,token=token)
        return Response("创建用户成功")

# 手动模拟 从数据库里拿到token 再访问http://127.0.0.1:8000/auth/test?token=160b85f738ca4869bc9ac2ec41e07709
class TestView(APIView):
    authentication_classes = [MyAuth,]   # 局部认证
    permission_classes = [MyPermission,] # 局部权限
    throttle_classes = [MyThrottle,]     # 限流
    def get(self,request):
        print(request.user)
        print(request.auth)
        user_id = request.user.id
        return Response('认证测试')

