from django.contrib import admin
from django.urls import path, include

from student.views import add_student,select_student,select2_student,index

urlpatterns = [
    path('add/', add_student),
    path('select/', select_student),
    path('select2/', select2_student),

]
