#!/usr/bin/env python
# -*- coding:utf-8 -*-

from stark.service.v1 import StarkHandler, get_choice_text, get_m2m_text, StarkModelForm
from web import models


class PublicCustomerModelForm(StarkModelForm):
    class Meta:
        model = models.Customer
        exclude = ['consultant', ]   # 公户排除录入课程顾问


class PublicCustomerHandler(StarkHandler):
    list_display = ['name', 'qq', get_m2m_text('咨询课程', 'course'), get_choice_text('状态', 'status')]

    def get_queryset(self, request, *args, **kwargs):
        return self.model_class.objects.filter(consultant__isnull=True)

    model_form_class = PublicCustomerModelForm
