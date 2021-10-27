from django import forms

from django.forms import widgets   # 导入自定义渲染类型
from app01.models import UserInfo

from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

class UserForm(forms.Form):
    name=forms.CharField(min_length=4,label="用户名",error_messages={"required":"该字段不能为空"},
                         widget=widgets.TextInput(attrs={"class":"form-control"})
                         )
    pwd=forms.CharField(min_length=4,label="密码",
                        widget=widgets.PasswordInput(attrs={"class":"form-control"})
                        )
    r_pwd=forms.CharField(min_length=4,label="确认密码",error_messages={"required":"该字段不能为空"},widget=widgets.TextInput(attrs={"class":"form-control"}))
    email=forms.EmailField(label="邮箱",error_messages={"required":"该字段不能为空","invalid":"格式错误"},widget=widgets.TextInput(attrs={"class":"form-control"}))
    tel=forms.CharField(label="手机号",widget=widgets.TextInput(attrs={"class":"form-control"}))


    def clean_name(self):  #  校验局部钩子(第二次校验), 命名规则  clean_字段名
        val=self.cleaned_data.get("name")  # 获取表单里用户输入的name值
        ret=UserInfo.objects.filter(name=val)   # 从数据库里查询
        if not ret:
            return val
        else:
            raise ValidationError("该用户已注册!")

    def clean_tel(self):
        val=self.cleaned_data.get("tel")
        if len(val)==11:
            return val
        else:
            raise  ValidationError("手机号格式错误")

    def clean(self):  # 校验全局钩子 clean
        pwd=self.cleaned_data.get('pwd')
        r_pwd=self.cleaned_data.get('r_pwd')
        if pwd and r_pwd:         # 判断两次密码上次是否校验成功, 获取none表示上次校验没有通过
            if pwd==r_pwd:        # 校验两次密码是否一致
                return self.cleaned_data
            else:
                raise ValidationError('两次密码不一致')
        else:
            return self.cleaned_data

