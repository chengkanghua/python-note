from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

from app01.models import UserInfo


def login(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        user = UserInfo.objects.filter(user=user, pwd=pwd).first()
        if user:
            # 登陆成功
            '''
            响应体:
            return HttpResponse()
            return render()
            return redirect()
            '''
            response = HttpResponse("登录成功!")
            # response.set_cookie("is_login",True,max_age=15)   #  超长时间15秒
            response.set_cookie("is_login", True)
            import datetime
            # date=datetime.datetime(year=2019,month=5,day=29,hour=14,minute=34)
            # response.set_cookie("username",user.user,expires=date) # expires 设置失效时间
            response.set_cookie("username", user.user, path="/index/")  # path= 设置有效路径
            return response

    return render(request, "login.html")


def index(request):
    print("index:", request.COOKIES)  # 打印cookies信息

    is_login = request.COOKIES.get("is_login")  # 获取 cookies里的is_login的值

    if is_login:
        username = request.COOKIES.get("username")
        import datetime
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  #当前日期
        last_time = request.COOKIES.get("last_visit_time", "") # 获取cookies里的 last_visit_time值,没有就空字符串
        response = render(request, "index.html", {"username": username, "last_time": last_time}) # render传给模板
        response.set_cookie("last_visit_time", now) # 设置cookies
        return response

    else:
        return redirect("/login/")


def test(request):
    print("test:", request.COOKIES)  # 不在有效路径拿不到 username值

    return HttpResponse("test!")


def login_session(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        user = UserInfo.objects.filter(user=user, pwd=pwd).first()
        if user:
            import datetime
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            request.session["is_login"] = True
            request.session["username"] = user.user
            request.session["last_visit_time"] = now
            # 背后发生如下操作
            '''
            if request.COOKIE.get("sessionid"):
                更新
                 在django—session表中创建一条记录:
                   session-key                                     session-data
                   ltv8zy1kh5lxj1if1fcs2pqwodumr45t                  更新数据
            else:
                1 生成随机字符串   ltv8zy1kh5lxj1if1fcs2pqwodumr45t
                2 response.set_cookie("sessionid",ltv8zy1kh5lxj1if1fcs2pqwodumr45t)
                3 在django—session表中创建一条记录:
                   session-key                                     session-data
                   ltv8zy1kh5lxj1if1fcs2pqwodumr45t       {"is_login":True,"username":"yuan"}

            '''
            return HttpResponse("登录成功!")

    return render(request, "login.html")


def index_session(request):
    print("is_login:", request.session.get("is_login"))   # 背后发生如下3步操作

    '''
    1  request.COOKIE.get("session")  #  ltv8zy1kh5lxj1if1fcs2pqwodumr45t
    2  django-session表中过滤纪录:
       在django—session表中创建一条记录:
               session-key                                   session-data
               ltv8zy1kh5lxj1if1fcs2pqwodumr45t       {"is_login":True,"username":"yuan"}
       obj=django—session.objects .filter(session-key=ltv8zy1kh5lxj1if1fcs2pqwodumr45t).first()
    3 obj.session-data.get("is_login")
    '''
    is_login = request.session.get("is_login")
    if not is_login:
        return redirect("/login_session/")
    username = request.session.get("username")
    last_visit_time = request.session.get("last_visit_time")

    return render(request, "index.html", {"username": username, "last_visit_time": last_visit_time})


def logout(request):
    # del request.session["is_login"]

    request.session.flush()
    # 背后做了如下三件事情
    '''
    1 randon_str=request.COOKIE.get("sessionid")
    2 django-session.objects.filter(session-key=randon_str).delete()
    3 response.delete_cookie("sessionid",randon_str)

    '''

    return redirect("/login/")
