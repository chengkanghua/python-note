from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

from cookie.models import User


def index(request):
    # 判断该客户端是否登录,读cookie
    is_login = request.get_signed_cookie("is_login", salt="12*$35867241")
    if is_login == "true":

        user_id = request.get_signed_cookie("user_id", salt="12*$35867241")
        user_name = User.objects.get(pk=user_id).name
        return render(request, "cookie/index.html", {"user_name": user_name})

    else:
        return redirect("/login")


def login(request):
    if request.method == "GET":
        return render(request, "cookie/login.html")

    else:
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        try:
            user = User.objects.get(name=user, pwd=pwd)

            res = redirect("/index")
            # 登录成功，写cookie
            # res.set_cookie("is_login", "true",max_age=10)
            # res.set_cookie("user_id", user.pk,max_age = 10)
            # res.set_cookie("is_login", "true")
            # res.set_cookie("user_id", user.pk)

            res.set_signed_cookie("is_login", "true", salt="12*$35867241")
            res.set_signed_cookie("user_id", user.pk, salt="12*$35867241")

            return res


        except Exception as e:

            return redirect("/login")
