from django import forms
from django.core.exceptions import ValidationError
from web.utils.md5 import gen_md5
from stark.service.v1 import StarkForm, StarkModelForm
from web import models


class UserInfoModelForm(StarkModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['nickname', 'phone', 'gender']


class ResetPasswordForm(StarkForm):
    orign_password = forms.CharField(
        label='原密码', widget=forms.PasswordInput, max_length=32)
    password = forms.CharField(
        label='新密码', widget=forms.PasswordInput, max_length=32)
    confirm_password = forms.CharField(
        label='重复密码', widget=forms.PasswordInput, max_length=32)

    # def clean_orign_password(self):
    #     id = 3
    #     orign_password = self.cleaned_data['orign_password']   
    #     if orign_password:
    #         orign_password = gen_md5(orign_password)
    #     user_obj = models.UserInfo.objects.filter(pk=id).first()
    #     if user_obj.password != orign_password:
    #         raise ValidationError('原密码输入错误')
    #     return orign_password

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


class LoginForm(StarkForm):
    user = forms.CharField(label='用户名', widget=forms.TextInput, max_length=32)
    pwd = forms.CharField(
        label='密码', widget=forms.PasswordInput, max_length=32)
