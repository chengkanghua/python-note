#!/usr/bin/env python
# -*- coding:utf-8 -*-
from stark.service.v1 import StarkHandler, get_datetime_text, get_m2m_text, StarkModelForm,Option
from stark.forms.widgets import DateTimePickerInput
from web import models


class ClassListModelForm(StarkModelForm):
    class Meta:
        model = models.ClassList
        fields = '__all__'
        widgets = {
            'start_date': DateTimePickerInput,
            'graduate_date': DateTimePickerInput,
        }


class ClassListHandler(StarkHandler):

    def display_course(self, obj=None, is_header=None):
        if is_header:
            return '班级'
        return "%s %s期" % (obj.course.name, obj.semester,)

    list_display = ['school', display_course, 'price', get_datetime_text('开班日期', 'start_date'), 'class_teacher',
                    get_m2m_text('任课老师', 'tech_teachers')]

    model_form_class = ClassListModelForm

    search_group = [
        Option('school'),
        Option('course'),
    ]
