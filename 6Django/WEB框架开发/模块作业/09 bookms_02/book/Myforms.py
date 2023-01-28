from django import forms
from django.forms import widgets
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.exceptions import NON_FIELD_ERRORS,ValidationError
class UserForm(forms.Form):
    user = forms.CharField(max_length=32,label='用户名',widget=widgets.TextInput(attrs={'class':'form-control'}))
    pwd  = forms.CharField(max_length=32,label='密码',widget=widgets.PasswordInput(attrs={'class':'form-control'}))
    re_pwd = forms.CharField(max_length=32,label='确认密码',widget=widgets.PasswordInput(attrs={'class':'form-control'}))

    def clean_user(self):  #局部钩子,第二次验证
        val = self.cleaned_data.get('user')
        user = User.objects.filter(username=val).exists()
        print(user)
        if not user:
            return val
        else:
            raise ValidationError("该用户已注册!")

    def clean(self): # 全局钩子,最后的验证
        pwd=self.cleaned_data.get("pwd")
        re_pwd=self.cleaned_data.get("re_pwd")

        if pwd and re_pwd:
            if pwd==re_pwd:
                return self.cleaned_data
            else:
                raise ValidationError("两次密码不一致!")
        else:
            return self.cleaned_data

