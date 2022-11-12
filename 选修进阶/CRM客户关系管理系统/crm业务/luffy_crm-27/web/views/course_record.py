#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.utils.safestring import mark_safe
from stark.service.v1 import StarkHandler, StarkModelForm, get_datetime_text
from web import models


class CourseRecordModelForm(StarkModelForm):
    class Meta:
        model = models.CourseRecord
        fields = ['day_num', 'teacher']


class CourseRecordHandler(StarkHandler):
    model_form_class = CourseRecordModelForm
    list_display = ['class_object', 'day_num', 'teacher', get_datetime_text('时间', 'date')]

    def display_edit_del(self, obj=None, is_header=None, *args, **kwargs):
        if is_header:
            return '操作'
        class_id = kwargs.get('class_id')
        tpl = '<a href="%s">编辑</a> <a href="%s">删除</a>' % (
            self.reverse_change_url(pk=obj.pk, class_id=class_id),
            self.reverse_delete_url(pk=obj.pk, class_id=class_id))
        return mark_safe(tpl)

    def get_urls(self):
        patterns = [
            url(r'^list/(?P<class_id>\d+)/$', self.wrapper(self.changelist_view), name=self.get_list_url_name),
            url(r'^add/(?P<class_id>\d+)/$', self.wrapper(self.add_view), name=self.get_add_url_name),
            url(r'^change/(?P<class_id>\d+)/(?P<pk>\d+)/$', self.wrapper(self.change_view),
                name=self.get_change_url_name),
            url(r'^delete/(?P<class_id>\d+)/(?P<pk>\d+)/$', self.wrapper(self.delete_view),
                name=self.get_delete_url_name),
        ]
        patterns.extend(self.extra_urls())
        return patterns

    def get_queryset(self, request, *args, **kwargs):
        class_id = kwargs.get('class_id')
        return self.model_class.objects.filter(class_object_id=class_id)

    def save(self, request, form, is_update, *args, **kwargs):
        class_id = kwargs.get('class_id')

        if not is_update:
            form.instance.class_object_id = class_id
        form.save()
