
from django import forms
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django.shortcuts import render, HttpResponse, reverse, redirect
from django.conf.urls import re_path
from django.http import QueryDict
from stark.service.v1 import site, StarkHandler, get_choice_text, StarkModelForm, StarkForm, Option, get_m2m_text
from web import models
from web.utils.md5 import gen_md5
from .base import PermissionHandler


class UserInfoAddModelForm(StarkModelForm):
    confirm_password = forms.CharField(label='确认密码', max_length=32)

    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'confirm_password', 'email', 'nickname',
                  'phone', 'gender', 'depart', 'roles']

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise ValidationError('两次密码不一致')
        return confirm_password

    def clean(self):  # 此方法在clean_field方法校验通过后执行？
        password = self.cleaned_data.get('password')
        if password:
            self.cleaned_data['password'] = gen_md5(password)
        return self.cleaned_data


class UserInfoChangeModelForm(StarkModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['name', 'email', 'nickname',
                  'phone', 'gender', 'depart', 'roles']


class ResetPasswordForm(StarkForm):
    password = forms.CharField(
        label='密码', widget=forms.PasswordInput, max_length=32)
    confirm_password = forms.CharField(
        label='重复密码', widget=forms.PasswordInput, max_length=32)

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise ValidationError('两次密码不一致')
        return confirm_password

    def clean(self):
        password = self.cleaned_data.get('password')
        if password:
            self.cleaned_data['password'] = gen_md5(password)
        return self.cleaned_data


class UserInfoHandler(PermissionHandler, StarkHandler):
    def display_reset_pwd(self, obj=None, is_header=None):
        if is_header:
            return "重置密码"

        return mark_safe('<a href="%s">重置密码</a>' % self.reverse_common_url(self.get_url_name('reset_pwd'), pk=obj.pk))

    list_display = ['nickname', get_choice_text('性别', 'gender'), 'phone',
                    'email', 'depart', get_m2m_text('角色', 'roles'), display_reset_pwd]

    search_list = ['nickname__contains', 'name__contains']

    search_group = [
        Option(field='gender'),
        Option(field='depart', is_multi=True)
    ]

    def get_model_form_class(self, is_add, request, *args, **kwargs):
        if is_add:
            return UserInfoAddModelForm
        return UserInfoChangeModelForm

    def reset_password(self, request, pk):
        """
        重置密码视图函数
        """
        userInfo_obj = models.UserInfo.objects.filter(pk=pk).first()
        if not userInfo_obj:
            return HttpResponse('该用户不存在，无法重置密码')
        if request.method == 'GET':
            form = ResetPasswordForm()
            return render(request, 'stark/change.html', {'form': form})
        form = ResetPasswordForm(data=request.POST)
        if form.is_valid():
            userInfo_obj.password = form.cleaned_data['password']
            userInfo_obj.save()
            return redirect(self.reverse_list_url())
        return render(request, 'stark/change.html', {'form': form})

    def extra_urls(self):
        patterns = [
            re_path(r'^reset/password/(?P<pk>\d+)/$',
                    self.wrapper(self.reset_password), name=self.get_url_name('reset_pwd')),
        ]
        return patterns
