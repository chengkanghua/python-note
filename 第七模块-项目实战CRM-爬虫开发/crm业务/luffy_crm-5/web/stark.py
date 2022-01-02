#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError
from stark.service.v1 import site, StarkHandler, get_choice_text, StarkModelForm
from web import models
from web.utils.md5 import gen_md5


class SchoolHandler(StarkHandler):
    list_display = ['title']


site.register(models.School, SchoolHandler)


class DepartmentHandler(StarkHandler):
    list_display = ['title', ]


site.register(models.Department, DepartmentHandler)


class UserInfoAddModelForm(StarkModelForm):
    confirm_password = forms.CharField(label='确认密码')

    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'confirm_password', 'nickname', 'gender', 'phone', 'email', 'depart', 'roles']

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise ValidationError('密码输入不一致')
        return confirm_password

    def clean(self):
        password = self.cleaned_data['password']
        self.cleaned_data['password'] = gen_md5(password)
        return self.cleaned_data


class UserInfoChangeModelForm(StarkModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['name', 'nickname', 'gender', 'phone', 'email', 'depart', 'roles']


class UserInfoHandler(StarkHandler):
    list_display = ['nickname', get_choice_text('性别', 'gender'), 'phone', 'email', 'depart']

    def get_model_form_class(self, is_add=False):
        if is_add:
            return UserInfoAddModelForm
        return UserInfoChangeModelForm


site.register(models.UserInfo, UserInfoHandler)
