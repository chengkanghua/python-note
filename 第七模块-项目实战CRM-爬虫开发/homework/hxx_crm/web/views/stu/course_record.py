# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect, reverse
from django.conf import settings
from web import models
import time, os


def list(request, classid):
    """作业列表"""
    print(classid)
    student_id = request.session['student_info']['id']
    student_obj = models.Student.objects.filter(pk=student_id).first()
    # 判断是否属于自己的课程
    classlist = student_obj.class_list.values_list('pk')
    if classid not in [i[0] for i in classlist]:
        return HttpResponse('课程信息不存在')
    # 获取课程信息
    class_obj = models.ClassList.objects.filter(pk=classid).first()
    # 获取作业表
    courserecord_list = models.CourseRecord.objects.filter(class_object=classid).all()
    print(courserecord_list)
    return render(request, 'student/course_list.html',
                  {
                      'courserecord_list': courserecord_list,
                      'class_obj': class_obj,
                  })


def edit(request, course_record_id):
    """提交作业"""
    # 获取作业信息
    course_record_obj = models.CourseRecord.objects.filter(pk=course_record_id).first()
    # 判断是否已交作业
    student_id = request.session['student_info']['id']
    study_record_obj = models.StudyRecord.objects.filter(course_record=course_record_id, student=student_id).first()
    print(study_record_obj)
    if request.method == 'GET':
        return render(request, 'student/course_record.html',
                      {'course_record_obj': course_record_obj, 'study_record_obj': study_record_obj})

    # 未考勤，无法提交作业
    if not study_record_obj:
        return HttpResponse('未生成考勤信息')
    # 已打分，不能重复提交
    if study_record_obj.homework_score:
        return HttpResponse('作业已打分，不能提交')
    # 作业文件上传
    homework_obj = request.FILES.get('homework')
    if not homework_obj:
        return render(request, 'student/course_record.html',
                      {'course_record_obj': course_record_obj, 'study_record_obj': study_record_obj, 'msg': '文件上传失败'})
    file_name = "%s.zip" % time.time()
    with open(file=os.path.join(settings.BASE_DIR, 'media', 'homework', file_name), mode="wb") as f:
        for line in homework_obj:
            f.write(line)
    study_record_obj.homework_url = file_name
    study_record_obj.save()
    return redirect(reverse('stu_course_list', kwargs={'classid': course_record_obj.class_object.pk}))
