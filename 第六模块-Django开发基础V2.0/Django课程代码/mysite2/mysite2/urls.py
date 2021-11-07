"""mysite2 URL Configuration

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
from django.urls import path, re_path,include

from articles.views import article_detail, article_archive_by_year, article_archive_by_month

from app01.views import show

from django.urls import register_converter

# 自定义路由转发器
class MobileConverter(object):
    # 正则规则
    regex = "1[3-9]\d{9}"

    def to_python(self,value):

        return int(value)

register_converter(MobileConverter,"mobile")


urlpatterns = [

    # ********************************   一 路由  ********************************

    # 请求路径和视图函数的映射关系,一旦请求路径和某一个path中的路径匹配成功，则调用该path中的视图函数
    # path('admin/', admin.site.urls),

    # 一一映射
    # path("timer/", get_timer),
    # path("", index),

    # 一对多映射:避免
    # path("timer/", index),
    # path("timer/", get_timer),

    # 多对一
    # path("timer/", get_timer),
    # path("", get_timer),

    # 正则和简单分组
    # path("articles/2012/", article_detail),
    # re_path("articles/(\d{4})$", article_archive_by_year),  # article_archive_by_year(request,2010)
    # re_path("articles/(\d{4})/(\d{1,2})", article_archive_by_month)  # article_archive_by_year(request,2010)

    # 有名分组
    # re_path("articles/(?P<year>\d{4})/(?P<month>\d{1,2})", article_archive_by_month),

    # 路由分发
    # path('home/', include('app01.urls')),
    # path('articles/', include('articles.urls')),

    # 路由转发器

    path("index/<mobile:m>",show),
    # ********************************   二 视图  ********************************
    path("users/",include("users.urls"))





]

'''

请求路径： /articles/2010/12

re.findall("articles/(\d{4})/(\d{1,2})","/articles/2010/12")


一旦匹配成功：

   if 是简单分组：
   
      调用article_archive_by_month(request,2010,12)

   else if 是有名分组：
   
      调用article_archive_by_month(request,year=2010,month=12)
        

'''
