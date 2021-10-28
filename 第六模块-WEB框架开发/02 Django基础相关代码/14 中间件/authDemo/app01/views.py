from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

from django.contrib import auth   # 导入auth模块
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def login(request):

    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        # 会去数据库里查, 验证成功返回user对象,否则返回None
        user=auth.authenticate(username=user,password=pwd)

        if user:
            auth.login(request,user)   # request.user:当前登录对象 全局变量,模块其他视图都可以调用

            next_url=request.GET.get("next","/index/")  # 获取跳转前的页面路径,没有就跳转index.
            return  redirect(next_url)


    return render(request,"login.html")



@login_required     # 登陆认证装饰器 未认证的将跳转到别的页面,在settings.py里配置 LOGIN_URL="跳转地址"
def index(request):

    # print("request.user:",request.user.username)
    # print("request.user:",request.user.id)
    # print("request.user:",request.user.is_anonymous)
    #
    # #if request.user.is_anonymous:    # 是否匿名用户
    # if not request.user.is_authenticated:  # 是否是认证用户
    #     return redirect("/login/")

    #username=request.user.username
    #return render(request,"index.html",{"username":username})

    return render(request,"index.html")


@login_required
def order(request):

    # if not request.user.is_authenticated:
    #     return redirect("/login/")

    return render(request,"order.html")



def logout(request):
    auth.logout(request)
    return redirect("/login/")




def reg(request):
    if request.method=="POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        #User.objects.create(username=user,password=pwd)
        user=User.objects.create_user(username=user,password=pwd)  # User对象创建用户

        return redirect("/login/")


    return render(request,"reg.html")


