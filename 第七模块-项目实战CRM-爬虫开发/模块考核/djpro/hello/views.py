from django.shortcuts import render,redirect,HttpResponse
from hello.models import User
from django.http import JsonResponse
# Create your views here.

def index(request):

    return HttpResponse('Hello World')
    # return render(request,'login.html')

def login(request):
    if request.is_ajax():
        # print(request.POST)
        response = {'state':None,'msg':None}
        name = request.POST.get('name')
        password = request.POST.get('pwd')
        user_obj = User.objects.filter(name=name,password=password).first()
        print(user_obj.name)
        if user_obj:
            request.session['user_info'] = user_obj.name

            response['state'] = True
        else:
            response['msg'] = 'user or password error!'
        return JsonResponse(response)
    return render(request, 'login.html')

def logout(request):
    # del request.session["user_info"]
    # 清空 session和cookie数据
    request.session.flush()
    # request.session.clear()
    # request.session.delete()
    return redirect('/login')


