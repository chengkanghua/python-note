from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import User
from django.http import JsonResponse
import json

import time


def reg(request):
    # time.sleep(10)
    return render(request, "reg.html")


def username_auth(request):
    time.sleep(10)
    print(request.POST)
    # 获取客户端数据：用户名
    username = request.POST.get("username")

    # 校验用户名是否存在
    res = {"exist": False, "msg": ""}
    ret = User.objects.filter(name=username)
    if ret:
        # 用户名存在
        res["exist"] = True
        res["msg"] = "该用户已经存在"

    # return HttpResponse(json.dumps(res))
    return JsonResponse(res)


def add(request):
    print(":::", request.POST)
    num1 = request.POST.get("num1")
    num2 = request.POST.get("num2")

    res = HttpResponse(str(int(num1) + int(num2)))
    res["Access-Control-Allow-Origin"] = "*"

    return res
