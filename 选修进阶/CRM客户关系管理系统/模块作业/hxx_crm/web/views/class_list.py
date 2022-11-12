from django import forms
from django.utils.safestring import mark_safe
from django.urls import reverse
from stark.service.v1 import StarkHandler, StarkModelForm, Option
from stark.service.v1 import get_datetime_text, get_m2m_text
from stark.forms.widgets import DatetimePickerInput
from web import models
from .base import PermissionHandler

class ClassListModelForm(StarkModelForm):
    class Meta:
        model = models.ClassList
        fields = '__all__'
        widgets = {
            'start_date': DatetimePickerInput,
            'graduate_date': DatetimePickerInput,
        }


class ClassListhandler(PermissionHandler, StarkHandler):
    def display_course(self, obj=None, is_header=None, *args, **kwargs):
        if is_header:
            return "课程"
        return '%s %s期' % (obj.course, obj.semester)

    def display_course_record(self, obj=None, is_header=None, *args, **kwargs):
        if is_header:
            return "上课记录"
        reverse_url = reverse("stark:web_courserecord_list", kwargs={'class_id': obj.pk})
        return mark_safe('<a href="%s" target="_blank">记录</a>' % reverse_url)


    list_display = ['school', display_course, 'price', get_datetime_text(
        '开班时间', 'start_date'), 'class_teacher', get_m2m_text('任课老师','tech_teachers'), display_course_record]
    
    model_form_class = ClassListModelForm

    search_group = {
        Option('school'),
        Option('course'),
    }
