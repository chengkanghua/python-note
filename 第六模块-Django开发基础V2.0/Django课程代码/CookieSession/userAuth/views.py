from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


import datetime
# 认证模块
from django.contrib import auth
# 对应数据库用户表,可以继承扩展



def index(request):


    # request.user:当前登录对象
    '''
    在AuthenticationMiddleware的process_request方法中,

       1. user_id = request.session.get("user_id")
       2. from django.contrib.auth.models import User
          user = User.objects.get(pk=user_id)
          if user:
             request.user = user

          else:
             request.user = AnonymousUser()  # 所有的属性都为零值


    结论：在任何视图函数中，都可以使用request.user
         如果之前登录成功过，即执行了auth.login(),那么request.user = 登录对象
         如果之前没有登录成功过，没有执行auth.login(),那么request.user = 匿名对象

    '''

    if request.user.username:
        # request.user的username不为零值，即登录成功过
        return render(request, "userAuth/index.html",{"user_name":request.user.username})

    else:
        return redirect("/userAuth/login")





def login(request):

    if request.method == "GET":
        return render(request, "userAuth/login.html")

    else:
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        # 将输入的密码转为密文去认证，认证成功返回用户对象，失败则返回None
        user = auth.authenticate(username=user, password=pwd)
        if user:
            #  登录成功

            # request.session["user_id"] = user.pk
            auth.login(request, user)

            return redirect("/userAuth/index")

        else:
            return redirect("/userAuth/login")


def logout(request):
    # request.session.flush()
    auth.logout(request)
    return redirect("/session/login")
