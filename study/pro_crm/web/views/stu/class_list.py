# -*- coding: utf-8 -*-
from django.shortcuts import HttpResponse, render, redirect
from web import models


def list(request):
    """学生所报班级列表"""
    student_id = request.session['student_info']['id']
    student_obj = models.Student.objects.filter(pk=student_id).first()
    classlist = student_obj.class_list.all()
    print(classlist)
    return render(request, 'student/class_list.html', {'classlist': classlist})

