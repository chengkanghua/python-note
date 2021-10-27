from django.shortcuts import render,HttpResponse,redirect
from app01.models import *
# Create your views here.

def index(request):

    return render(request,"index.html")

def test_ajax(request):
    print(request.GET)
    return HttpResponse("hello ok")

def cal(request):
    print(request.POST)
    n1 = int(request.POST.get("n1"))
    n2 = int(request.POST.get("n2"))
    data = n1 + n2
    return HttpResponse(data)

def login(request):
    uname = request.POST.get("uname")
    password = request.POST.get("password")
    print(uname,password)
    user_obj = User.objects.filter(uname=uname,password=password).first()
    print(user_obj)
    res = {"uname":None,"msg":None}
    if user_obj:
        res["uname"] = user_obj.uname
    else:
        res["msg"] = "user or password wrong!"

    import json
    return HttpResponse(json.dumps(res))

def file_put(request):
    if request.method == 'POST':
        print(request.body)
        print(request.POST)

        print(request.FILES)
        file_obj = request.FILES.get("avatar")
        print(file_obj)
        with open(file_obj.name,"wb") as f:
            for line in file_obj:
                f.write(line)
        return HttpResponse("ok")
    return render(request,"file_put.html")