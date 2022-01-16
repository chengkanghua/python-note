"""pro_crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url,include
from django.conf import settings
from stark.service.v1 import site
from django.views.static import serve
from web.views import account
from web.views.stu import student, class_list, course_record

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stark/',site.urls),
    re_path(r'^rbac/', include(('rbac.urls','rbac'), namespace='rbac')),
    path('login/',account.login,name='login'),
    path('logout/',account.logout,name='logout'),
    path('index/',account.index,name='index'),
    path('info/', account.info, name='info'),
    path('password/', account.password, name='password'),


    # 学生端url
    path('stu_login/', student.login, name='stu_login'),
    path('stu/logout/', student.logout, name='stu_logout'),
    path('stu/index/', student.index, name='stu_index'),
    path('stu/classlist/', class_list.list, name='stu_classlist'),
    path('stu/course_record/list/<int:classid>/', course_record.list, name='stu_course_list'),
    path('stu/course_record/edit/<int:course_record_id>/', course_record.edit, name='stu_course_edit'),

    # 默认首页
    re_path(r'^$', account.guide),

    # 配置media
    re_path(r"^%s(?P<path>.*)$" % settings.MEDIA_URL.lstrip('/'), serve,
            {"document_root": settings.MEDIA_ROOT}),

    # re_path(r"^media/(?P<path>.*)$", serve,
    #         {"document_root": settings.MEDIA_ROOT}),
]
