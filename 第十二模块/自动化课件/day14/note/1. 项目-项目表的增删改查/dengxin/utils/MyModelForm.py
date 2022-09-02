from django.forms import ModelForm
from django import forms
from django.forms import widgets as wid
from app01 import models


class ItModelForm(ModelForm):
    class Meta:
        model = models.It
        fields = "__all__"
        # 法2
        labels = {
            "it_name": "项目名称",
            "it_desc": "项目描述",
            "it_start_tile": "项目开始时间",
            "it_end_tile": "项目结束时间",
        }
        error_messages = {
            "it_name": {"required": "不能为空"},
            "it_desc": {"required": "不能为空"},
            "it_start_tile": {"required": "不能为空"},
            "it_end_tile": {"required": "不能为空"},
        }
        widgets = {
            "it_name": wid.Input(attrs={"class": "form-control", "placeholder": "输入项目名称"}),
            "it_desc": wid.Textarea(attrs={"class": "form-control", "placeholder": "输入项目名称"}),
            "it_start_time": wid.DateInput(attrs={"class": "form-control", 'type': "date"}),
            "it_end_time": wid.DateInput(attrs={"class": "form-control", 'type': "date"}),
        }

    # bootstrapClass_filter = ['it_start_time', 'it_end_time']
    # it_start_time = forms.DateField(label="开始时间", widget=wid.DateInput(attrs={"class": "form-control", 'type': "date"}))
    # it_end_time = forms.DateField(label="结束时间", widget=wid.DateInput(attrs={"class": "form-control", 'type': "date"}))
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for name, field in self.fields.items():
    #         if name in self.bootstrapClass_filter:
    #             continue
    #         old_class = field.widget.attrs.get('class', "")
    #         field.widget.attrs['class'] = '{} form-control'.format(old_class)
    #         field.widget.attrs['placeholder'] = '请输入%s' % (field.label,)