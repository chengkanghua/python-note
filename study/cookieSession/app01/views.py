from django.shortcuts import render, HttpResponse, redirect
from app01.models import UserInfo


# Create your views here.

def login(request):
    if request.method == 'POST':
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        user = UserInfo.objects.filter(user=user, pwd=pwd).first()
        if user:
            response = HttpResponse("登陆成功")
            # response.set_cookie("is_login",True,max_age=15)
            response.set_cookie("is_login", True)
            response.set_cookie('username', user.user, path="/index/")
            return response
    return render(request, "login.html")


def index(request):
    print(request.COOKIES)
    is_login = request.COOKIES.get('is_login')
    if is_login:
        username = request.COOKIES.get('username')
        import datetime
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        last_visit_time = request.COOKIES.get("last_visit_time")
        response = render(request, "index.html", {"username": username, "last_visit_time": last_visit_time})
        response.set_cookie("last_visit_time", now)
        return response
    else:
        return redirect("/login/")

    return render(request, "index.html")


def test(requset):
    print("test", requset.COOKIES)
    return HttpResponse("test")


def index_session(request):
    print("is_login", request.session.get('is_login'))

    is_login = request.session.get("is_login")
    if not is_login:
        return redirect('/login_session/')
    username = request.session.get("username")
    last_visit_time = request.session.get("last_visit_time")
    return render(request, 'index.html',{'username':username,"last_visit_time":last_visit_time})


def login_session(request):
    if request.method == 'POST':
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        user = UserInfo.objects.filter(user=user, pwd=pwd).first()
        if user:
            import datetime
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            request.session['is_login'] = True
            request.session['username'] = user.user
            request.session['last_visit_time'] = now

            return HttpResponse("登陆成功")
        return render(request, 'index.html')
    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return redirect('/login/')

def index1(request):
    is_login = request.session.get("is_login")
    username = request.session.get("username")
    last_visit_time = request.session.get("last_visit_time")
    if not is_login:
        username = '您还没有登陆'
        return render(request, 'index2.html', {"username": username})
    return render(request, 'index1.html', {'username': username, "last_visit_time": last_visit_time})


def index2(request):
    is_login = request.session.get("is_login")
    username = request.session.get("username")
    last_visit_time = request.session.get("last_visit_time")
    if not is_login:
        username = '您还没有登陆'
        return render(request,'index2.html',{"username":username})
    return render(request, 'index2.html', {'username': username, "last_visit_time": last_visit_time})
