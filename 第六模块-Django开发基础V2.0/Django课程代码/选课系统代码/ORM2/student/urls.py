from django.contrib import admin
from django.urls import path, include, re_path

from student.views import index, add_student, delete_student,edit_student,elective

urlpatterns = [
    path("", index),
    path("add/", add_student),
    re_path("delete/(\d+)", delete_student),
    re_path("edit/(\d+)", edit_student),

    # 选课
    re_path("elective/", elective),


]
