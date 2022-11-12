#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from stark.service.v1 import StarkHandler, StarkModelForm
from web import models


class ConsultRecordModelForm(StarkModelForm):
    class Meta:
        model = models.ConsultRecord
        fields = ['note', ]


class ConsultRecordHandler(StarkHandler):
    change_list_template = 'consult_record.html'
    model_form_class = ConsultRecordModelForm

    list_display = ['note', 'consultant', 'date']

    def get_urls(self):
        patterns = [
            url(r'^list/(?P<customer_id>\d+)/$', self.wrapper(self.changelist_view), name=self.get_list_url_name),
            url(r'^add/(?P<customer_id>\d+)/$', self.wrapper(self.add_view), name=self.get_add_url_name),
            url(r'^change/(?P<pk>\d+)/$', self.wrapper(self.change_view), name=self.get_change_url_name),
            url(r'^delete/(?P<pk>\d+)/$', self.wrapper(self.delete_view), name=self.get_delete_url_name),
        ]

        patterns.extend(self.extra_urls())
        return patterns

    def get_queryset(self, request, *args, **kwargs):
        customer_id = kwargs.get('customer_id')
        current_user_id = request.session['user_info']['id']
        return self.model_class.objects.filter(customer_id=customer_id, customer__consultant_id=current_user_id)

    def save(self, request, form, is_update, *args, **kwargs):
        if not is_update:
            customer_id = kwargs.get('customer_id')
            current_user_id = request.session['user_info']['id']
            form.instance.customer_id = customer_id
            form.instance.consultant_id = current_user_id
        form.save()
