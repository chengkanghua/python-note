#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.forms import ModelForm, Form
from web import models


class CustomerForm(ModelForm):
    class Meta:
        model = models.Customer   # 对应的Model中的类
        fields = "__all__"        # 字段，如果是__all__,就是表示列出所有的字段

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():    # 遍历所有字段加上html属性
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

