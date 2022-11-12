from django.shortcuts import HttpResponse
from django.conf.urls import url
from stark.service.v1 import site,StarkHandler,get_choice_text,StarkModelForm,Option
from django import forms
from app01 import models

class DepartHandler(StarkHandler):
    list_display = [StarkHandler.display_checkbox,'id','title',StarkHandler.display_edit,StarkHandler.display_del]
    has_add_btn = True
    action_list = [StarkHandler.action_multi_delete, ]

site.register(models.Depart,DepartHandler)

class UserInfoModelForm(StarkModelForm):
    # xx = forms.CharField() # 自定义字段
    class Meta:
        model = models.UserInfo
        fields = ['name','gender','classes','age','email']

class MyOption(Option):
    def get_db_condition(self,request,*args,**kwargs):
        return {}
class UserInfoHandler(StarkHandler):
    # 定制页面显示的列
    list_display = [StarkHandler.display_checkbox,
                    'name',
                    get_choice_text('性别', 'gender'),
                    get_choice_text('班级', 'classes'),
                    'age', 'email', 'depart',
                    StarkHandler.display_edit,
                    StarkHandler.display_del]
    per_page_count = 5  # 每页显示数量
    has_add_btn = True   # 显示添加按钮
    # model_form_class = UserInfoModelForm
    action_list = [StarkHandler.action_multi_delete, ]
    order_list = ['id']
    # 姓名或邮箱中包含关键字
    search_list = ['name__contains','email__contains']

    # def save(self,form, is_update=False):
    #     form.instance.depart_id = 1
    #     form.save()
    search_group = [
        Option('gender',is_multi=True),
        Option('depart',)
        # MyOption('depart', {'id__gt': 2}),
        # Option('gender', text_func=lambda field_object: field_object[1] + '666'),
    ]
site.register(models.UserInfo, UserInfoHandler)

####### Deploy 表操作 ######
class DeployHandler(StarkHandler):
    list_display = ['title',get_choice_text('状态','status'),StarkHandler.display_edit,StarkHandler.display_del]
    per_page_count = 2

site.register(models.Deploy,DeployHandler)
