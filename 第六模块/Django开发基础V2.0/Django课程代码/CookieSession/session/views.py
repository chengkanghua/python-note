from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

from session.models import User
import datetime


def index(request):
    # 读session
    # 1. 取session_id的钥匙
    # 2. 去django-session表中查询符合条件的记录
    # 3. 将取出的session-data.get("user_id")
    user_id = request.session.get("user_id")

    if user_id:
        #  登录成功过
        user = User.objects.get(pk=user_id)

        return render(request, "session/index.html", {"user_name": user.name})
    else:
        return redirect("/session/login")


def login(request):
    if request.method == "GET":
        return render(request, "session/login.html")

    else:
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        try:
            user = User.objects.get(name=user, pwd=pwd)
            # 写session
            # 1.创建随机字符串
            # 2.将随机字符串作为session-key，将session键值对作为session-data插入到django-session表中
            # 3.将session_id和随机字符串组成键值作为cookie返回给客户端

            request.session["user_id"] = user.pk

            return redirect("/session/index")


        except Exception as e:
            return redirect("/session/login")


def shop(request):
    # 取上一次的访问时间
    last_visit_time = request.session.get("last_visit_time", "第一次访问")
    # 将当前时间设置到session中保存，作为最后一次的访问时间
    now = datetime.datetime.now().strftime("%Y/%m/%d %X")
    request.session["last_visit_time"] = now

    return render(request, "session/shop.html", {"last_visit_time": last_visit_time})


def logout(request):
    # 删除session

    # 删除整条记录,同时删除session_id的cookie
    # request.session.flush()
    del request.session["user_id"]

    return redirect("/session/login")
