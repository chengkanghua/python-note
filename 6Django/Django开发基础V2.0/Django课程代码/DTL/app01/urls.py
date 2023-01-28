from django.contrib import admin
from django.urls import path, include

from app01.views import index, order

urlpatterns = [

    path('index/', index, name="ind"),
    path('order/', order, name="ord"),  # name是路径名字, 起到反向解析的作用, 模板里连接写 /ord/ 会跳转到这个路径

]


