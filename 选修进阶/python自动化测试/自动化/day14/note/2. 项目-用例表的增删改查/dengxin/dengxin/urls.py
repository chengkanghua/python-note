"""dengxin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    # 项目表相关的
    url(r'^index/', views.index, name='index'),
    url(r'^add_it/', views.add_it, name='add_it'),
    url(r'^edit_it/(?P<pk>\d+)$', views.edit_it, name='edit_it'),
    url(r'^delete_it/(?P<pk>\d+)$', views.delete_it, name='delete_it'),

    # 接口用例表相关
    url(r'^list_api/(?P<pk>\d+)$', views.list_api, name='list_api'),
    url(r'^add_api/(?P<pk>\d+)$', views.add_api, name='add_api'),
    url(r'^edit_api/(?P<pk>\d+)$', views.edit_api, name='edit_api'),
    url(r'^delete_api/(?P<pk>\d+)$', views.delete_api, name='delete_api'),
]
