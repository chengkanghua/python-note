#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.shortcuts import HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe
from stark.service.v1 import site, StarkHandler, get_choice_text, StarkModelForm
from django import forms
from app01 import models


# http://127.0.0.1:8000/stark/app01/depart/list/
class DepartHandler(StarkHandler):
    list_display = ['id', 'title', StarkHandler.display_edit, StarkHandler.display_del]
    has_add_btn = True


site.register(models.Depart, DepartHandler)


# http://127.0.0.1:8000/stark/app01/userinfo/list/

class UserInfoModelForm(StarkModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['name', 'gender', 'classes', 'age', 'email']


class UserInfoHandler(StarkHandler):
    # 定制页面显示的列
    list_display = ['name',
                    get_choice_text('性别', 'gender'),
                    get_choice_text('班级', 'classes'),
                    'age', 'email', 'depart',
                    StarkHandler.display_edit,
                    StarkHandler.display_del]

    per_page_count = 10

    has_add_btn = True

    model_form_class = UserInfoModelForm

    def save(self, form, is_update=False):
        form.instance.depart_id = 1
        form.save()


site.register(models.UserInfo, UserInfoHandler)


# ############# Deploy 表操作 #############
class DeployHandler(StarkHandler):
    list_display = ['title', get_choice_text('状态', 'status'), StarkHandler.display_edit, StarkHandler.display_del]


site.register(models.Deploy, DeployHandler)
