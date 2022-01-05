from django.urls import re_path
from django import forms
from django.shortcuts import HttpResponse
from django.core.exceptions import ValidationError
from stark.service.v1 import StarkHandler, StarkModelForm, get_choice_text
from web import models
from web.utils.md5 import gen_md5
from .base import PermissionHandler
import re


class PaymentRecordModelForm(StarkModelForm):
    class Meta:
        model = models.PaymentRecord
        fields = ['pay_type', 'paid_fee', 'class_list', 'note']


class StudentPaymentRecordModelForm(StarkModelForm):  # 包含学生信息的modelform
    qq = forms.CharField(label='QQ号', max_length=32)
    mobile = forms.CharField(label='手机号', max_length=32)
    emergency_contract = forms.CharField(label='紧急联系人电话', max_length=32)

    class Meta:
        model = models.PaymentRecord
        fields = ['pay_type', 'paid_fee', 'class_list',
                  'qq', 'mobile', 'emergency_contract', 'note']

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        reg = '^1[3|5|7|8|9][0-9]{9}$'
        if not re.findall(reg, mobile):
            raise ValidationError('手机号码有误')
        # 手机号码是否重复
        return mobile


class PamentRecordHandler(PermissionHandler, StarkHandler):
    list_display = [get_choice_text('缴费类型', 'pay_type'), 'paid_fee', 'class_list', 'consultant',
                    get_choice_text('状态', 'confirm_status', 'color:red')]

    # 重写按钮显示，去除修改，删除按钮
    def get_list_display(self, request, *args, **kwargs):
        value = []
        value.extend(self.list_display)
        return value

    # 重构，url ， 每个用户 的跟进记录都有一条url
    def get_urls(self):  # 重写url
        patterns = [
            re_path(r'^list/(?P<customer_id>\d+)/$',
                    self.wrapper(self.changelist_view), name=self.get_list_url_name),
            re_path(r'^add/(?P<customer_id>\d+)/$',
                    self.wrapper(self.add_view), name=self.get_add_url_name),
        ]
        patterns.extend(self.extra_urls())
        return patterns

    # 重写,只能看到自己私户信息的记录
    def get_queryset(self, request, *args, **kwargs):
        customer_id = kwargs.get('customer_id')  # 取到具体哪个学员过滤
        # 获取session中的当前用户id，只有当前用户才能看自己的管理学员跟进
        current_user_id = request.session['user_info']['id']
        return self.model_class.objects.filter(customer_id=customer_id, customer__consultant_id=current_user_id)

    # model_form_class = PaymentRecordModelForm
    def get_model_form_class(self, is_add, request, *args, **kwargs):
        customer_id = kwargs.get('customer_id')
        student_exists = models.Student.objects.filter(
            customer_id=customer_id).exists()
        if student_exists:
            # 说明已经存在，就用 普通modelform
            return PaymentRecordModelForm

        return StudentPaymentRecordModelForm

    def save(self, request, form, is_update, *args, **kwargs):  # 重写模块中的方法
        # 默认添加学员是给当前id的销售顾问
        customer_id = kwargs.get('customer_id')
        current_user_id = request.session['user_info']['id']
        object_exists = models.Customer.objects.filter(
            id=customer_id, consultant_id=current_user_id).exists()
        if not object_exists:
            return HttpResponse("非法操作")
        # 创建缴费记录信息
        form.instance.customer_id = customer_id
        form.instance.consultant_id = current_user_id
        form.save()  # 保存
        # 保存用户信息
        class_list = form.cleaned_data['class_list']
        fetch_student_object = models.Student.objects.filter(customer_id=customer_id).first()
        if not fetch_student_object:
            qq = form.cleaned_data['qq']
            mobile = form.cleaned_data['mobile']
            emergency_contract = form.cleaned_data['emergency_contract']
            password = gen_md5(mobile[5:])  # 学生账户初始密码为：手机号码后6位
            # 判断是否存在
            mobile_exist = models.Student.objects.filter(mobile=mobile).exists()
            if mobile_exist:
                return HttpResponse('该手机号码/账号已存在')

            student_object = models.Student.objects.create(customer_id=customer_id, qq=qq, mobile=mobile,
                                                           emergency_contract=emergency_contract, password=password)
            student_object.class_list.add(class_list)
        else:
            fetch_student_object.class_list.add(class_list)
