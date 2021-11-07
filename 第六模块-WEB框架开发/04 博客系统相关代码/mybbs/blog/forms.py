#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/5/19

"""
blog相关form
"""

from django import forms
from django.forms import widgets
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class RegForm(forms.Form):
    username = forms.CharField(
        # 校验规则相关
        max_length=16,
        label="用户名",
        error_messages={
            "required": "该字段不能为空",
        },
        # widget控制的是生成html代码相关的
        widget=widgets.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        label="密码",
        min_length=6,
        max_length=10,
        widget=widgets.PasswordInput(attrs={"class": "form-control"}, render_value=True),
        error_messages={
            "min_length": "密码不能少于6位！",
            "max_length": "密码最长10位！",
            "required": "该字段不能为空",
        }
    )
    re_password = forms.CharField(
        label="确认密码",
        min_length=6,
        max_length=10,
        widget=widgets.PasswordInput(attrs={"class": "form-control"}, render_value=True),
        error_messages={
            "min_length": "密码不能少于6位！",
            "max_length": "密码最长10位！",
            "required": "该字段不能为空",
        }
    )

    phone = forms.CharField(
        label="手机",
        # 自己定制校验规则
        validators=[
            RegexValidator(r'^[0-9]+$', '手机号必须是数字'),
            RegexValidator(r'^1[3-9][0-9]{9}$', '手机格式有误')
        ],
        widget=widgets.TextInput(attrs={"class": "form-control"}),
        error_messages={
            "required": "该字段不能为空",
        }
    )

    def clean_username(self):
        value = self.cleaned_data.get("username")
        if "金瓶梅" in value:
            self.add_error("username", ValidationError("不符合社会主义核心价值观！"))
        # 重写局部钩子方法时一定要注意，没有报错要将对应的值返回
        else:
            return value

    # 重写父类的clean方法
    def clean(self):
        # 此时 通过检验的字段的数据都保存在 self.cleaned_data
        pwd = self.cleaned_data.get("pwd")
        re_pwd = self.cleaned_data.get("re_pwd")
        if pwd != re_pwd:
            self.add_error("re_pwd", ValidationError("两次密码不一致"))
            self.add_error("re_password", ValidationError("两次密码不一致"))
        # 重写全局钩子方法时一定要注意，没有报错要将 self.cleaned_data 返回
        else:
            return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(
        # 校验规则相关
        max_length=16,
        label="用户名",
        error_messages={
            "required": "该字段不能为空",
        },
        # widget控制的是生成html代码相关的
        widget=widgets.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        label="密码",
        min_length=6,
        max_length=10,
        widget=widgets.PasswordInput(attrs={"class": "form-control"}, render_value=True),
        error_messages={
            "min_length": "密码不能少于6位！",
            "max_length": "密码最长10位！",
            "required": "该字段不能为空",
        }
    )
