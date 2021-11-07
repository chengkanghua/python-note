#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/5/21

from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'poll/', views.poll),
    url(r'comment/', views.comment),
    url(r'(\w+)/(tag|category|archive)/(.+)/', views.home),
    url(r'(\w+)/article/(\d+)/', views.article_detail),
    # 管理后台
    url(r'backend/', views.backend),
    # 添加博客
    url(r'add/', views.add_article),
    # 编辑或删除
    url(r'(edit|delete)/(\d+)', views.op_article),
    url(r'(\w+)/$', views.home),
]
