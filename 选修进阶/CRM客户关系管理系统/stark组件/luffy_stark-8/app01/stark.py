#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.shortcuts import HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe
from stark.service.v1 import site, StarkHandler, get_choice_text
from app01 import models


# http://127.0.0.1:8000/stark/app01/depart/list/
class DepartHandler(StarkHandler):
    list_display = ['id', 'title', StarkHandler.display_edit, StarkHandler.display_del]


site.register(models.Depart, DepartHandler)


# http://127.0.0.1:8000/stark/app01/userinfo/list/
class UserInfoHandler(StarkHandler):
    # 定制页面显示的列
    list_display = ['name',
                    get_choice_text('性别', 'gender'),
                    get_choice_text('班级', 'classes'),
                    'age', 'email', 'depart',
                    StarkHandler.display_edit,
                    StarkHandler.display_del]

    per_page_count = 1


site.register(models.UserInfo, UserInfoHandler)
