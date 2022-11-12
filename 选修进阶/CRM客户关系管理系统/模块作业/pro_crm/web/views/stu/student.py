# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, reverse, HttpResponse
from web import models
from web.utils.md5 import gen_md5



def index(request):
    """学生中心首页"""
    return render(request, 'student/index.html')


def login(request):
    """学生用户登录"""
    if request.method == 'GET':
        return render(request, 'student/login.html')
    mobile = request.POST.get('mobile')
    password = request.POST.get('password')
    # 根据用户名和密码去用户表中获取用户对象
    student = models.Student.objects.filter(mobile=mobile, password=gen_md5(password)).first()
    if not student:
        return render(request, 'student/login.html', {'msg': '用户名或密码错误'})
    request.session['student_info'] = {'id': student.id, 'name': student.customer.name}

    return redirect('/stu/index/')


def logout(request):
    """学生用户登出"""
    request.session.delete()
    return redirect('/stu_login/')
