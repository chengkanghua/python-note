#!/usr/bin/env python
# -*- coding:utf-8 -*-
from stark.service.v1 import site, StarkHandler, get_choice_text, StarkModelForm
from web import models


class SchoolHandler(StarkHandler):
    list_display = ['title']

site.register(models.School, SchoolHandler)

class DepartmentHandler(StarkHandler):
    list_display = ['title', ]

site.register(models.Department, DepartmentHandler)

class UserInfoModelForm(StarkModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'nickname', 'gender', 'phone', 'email', 'depart', 'roles']


class UserInfoHandler(StarkHandler):
    list_display = ['nickname', get_choice_text('性别', 'gender'), 'phone', 'email', 'depart']
    model_form_class = UserInfoModelForm

site.register(models.UserInfo, UserInfoHandler)
