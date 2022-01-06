from django.shortcuts import render,HttpResponse,redirect
from web import models
from web.utils.md5 import gen_md5
from rbac.service.init_permission import init_permission
from web.forms.userinfo import UserInfoModelForm,ResetPasswordForm
from django.urls import reverse


def guide(request):
    """系统引导页"""
    return render(request, 'guide.html')

def login(request):
    '''
    用户登录
    :param request:
    :return:
    '''
    print(request.path_info)
    if request.method == 'GET':
        return render(request,'login.html')

    user = request.POST.get('user')
    pwd = gen_md5(request.POST.get('pwd',''))

    # 根据用户名和密码去用户表中获取用户对象
    user = models.UserInfo.objects.filter(name=user,password=pwd).first()
    if not user:
        return render(request,'login.html',{'msg':'用户名或密码错误'})
    request.session['user_info'] = {'id':user.id, 'nickname': user.nickname}
    # 用户权限信息的初始化
    init_permission(user, request)
    return redirect('/index/')

def logout(request):
    '''
    注销
    :param request:
    :return:
    '''
    request.session.delete()
    return redirect('/login')

def index(request):
    """管理后台首页"""
    return render(request,'index.html')


def info(request):
    """个人信息修改"""
    current_user_id = request.session['user_info']['id']
    user_obj = models.UserInfo.objects.filter(pk=current_user_id).first()
    if request.method == 'GET':
        form = UserInfoModelForm(instance=user_obj)
        return render(request, 'change.html', {'form': form})

    form = UserInfoModelForm(data=request.POST, instance=user_obj)
    if form.is_valid():
        form.save()
        return redirect(reverse('info'))
    else:
        return render(request, 'change.html', {'form': form})


def password(request):
    """个人密码修改"""
    if request.method == 'GET':
        form = ResetPasswordForm()
        return render(request, 'change.html', {'form': form})
    form = ResetPasswordForm(data=request.POST)
    print(form)
    if form.is_valid():
        current_user_id = request.session['user_info']['id']
        user_obj = models.UserInfo.objects.filter(pk=current_user_id).first()
        print(user_obj.password)
        print(form.cleaned_data['orign_password'])
        if user_obj.password != form.cleaned_data['orign_password']:
            return HttpResponse('原密码输入错误')
        user_obj.password = form.cleaned_data['password']
        user_obj.save()
        return redirect(reverse('password'))
    else:
        return render(request, 'change.html', {'form': form})

