#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.shortcuts import HttpResponse
from stark.service.v1 import site, StarkHandler
from app01 import models


# http://127.0.0.1:8000/stark/app01/depart/list/
class DepartHandler(StarkHandler):
    list_display = ['title']


site.register(models.Depart, DepartHandler)


# http://127.0.0.1:8000/stark/app01/userinfo/list/
class UserInfoHandler(StarkHandler):
    # 定制页面显示的列
    list_display = ['name', 'age', 'email']


site.register(models.UserInfo, UserInfoHandler)
