#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.utils.safestring import mark_safe
from django.conf.urls import url
from django.shortcuts import HttpResponse, render
from stark.service.v1 import StarkHandler, get_choice_text, get_m2m_text, StarkModelForm
from web import models


class PublicCustomerModelForm(StarkModelForm):
    class Meta:
        model = models.Customer
        exclude = ['consultant', ]


class PublicCustomerHandler(StarkHandler):

    def display_record(self, obj=None, is_header=None):
        if is_header:
            return '跟进记录'
        record_url = self.reverse_commons_url(self.get_url_name('record_view'), pk=obj.pk)
        return mark_safe('<a href="%s">查看跟进</a>' % record_url)

    list_display = ['name', 'qq', get_m2m_text('咨询课程', 'course'), display_record, get_choice_text('状态', 'status')]

    def get_queryset(self, request, *args, **kwargs):
        return self.model_class.objects.filter(consultant__isnull=True)

    model_form_class = PublicCustomerModelForm

    def extra_urls(self):
        patterns = [
            url(r'^record/(?P<pk>\d+)/$', self.wrapper(self.record_view),
                name=self.get_url_name('record_view')),
        ]
        return patterns

    def record_view(self, request, pk):
        """
        查看跟进记录的视图
        :param request:
        :param pk:
        :return:
        """
        record_list = models.ConsultRecord.objects.filter(customer_id=pk)
        return render(request, 'record_view.html', {'record_list': record_list})
