from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.base_response import BaseResponse
from .models import User
from utils.redis_pool import POOL
import redis
import uuid
# Create your views here.

class LoginView(APIView):
    def post(self,request):
        res = BaseResponse()
        print(request.data)
        username = request.data.get('username','')
        password = request.data.get('password','')
        user_obj = User.objects.filter(name=username,password=password).first()
        if not user_obj:
            res.code = 1030
            res.error = '账号或者密码错误'
            return Response(res.dict)
        conn = redis.Redis(connection_pool=POOL)
        token = uuid.uuid4()
        # conn.set(str(token), user_obj.id, ex=900) # 900秒过期
        conn.set(str(token), user_obj.id)
        res.access_token = token
        res.username = username
        res.data = '登陆成功'
        return Response(res.dict)

class LogoutView(APIView):
    def post(self,request):
        res = BaseResponse()
        access_token = request.data.get('access_token')
        conn = redis.Redis(connection_pool=POOL)
        reply = conn.delete(access_token)   # reply  1 成功删除   0 表示不存在的值
        res.code = 1000
        res.data = '退出成功'
        return Response(res.dict)