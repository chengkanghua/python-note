# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError
from web import models
from web.utils.md5 import gen_md5
from stark.service.v1 import StarkForm, StarkModelForm
import re


class StudentModelForm(StarkModelForm):
    """自定义显示指定字段"""

    class Meta:
        model = models.Student
        fields = ['mobile', 'qq', 'emergency_contract', 'score', 'memo']

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        reg = '^1[3|5|7|8|9][0-9]{9}$'
        if not re.findall(reg, mobile):
            raise ValidationError('手机号码有误')
        # 手机号码是否重复
        return mobile


class ResetPasswordForm(StarkForm):
    password = forms.CharField(
        label='新密码', widget=forms.PasswordInput, max_length=32)
    confirm_password = forms.CharField(
        label='重复密码', widget=forms.PasswordInput, max_length=32)

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise ValidationError('两次密码不一致')
        return confirm_password

    def clean(self):
        password = self.cleaned_data.get('password')
        if password:
            self.cleaned_data['password'] = gen_md5(password)
        return self.cleaned_data
