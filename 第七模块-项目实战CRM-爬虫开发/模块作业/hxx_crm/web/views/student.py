from stark.service.v1 import StarkHandler, get_choice_text, StarkModelForm, get_m2m_text, get_another_text, Option
from django.conf.urls import re_path
from django.shortcuts import reverse, HttpResponse, render, redirect
from django.utils.safestring import mark_safe
from web import models
from web.forms.student import StudentModelForm, ResetPasswordForm
from .base import PermissionHandler


class StudentHandler(PermissionHandler, StarkHandler):
    model_form_class = StudentModelForm
    has_add_btn = False

    def display_reset_pwd(self, obj=None, is_header=None):
        if is_header:
            return "重置密码"
        return mark_safe('<a href="%s">重置密码</a>' % self.reverse_common_url(self.get_url_name('reset_pwd'), pk=obj.pk))

    def display_score(self, obj=None, is_header=None, *args, **kwargs):
        """新加积分管理一列"""
        if is_header:
            return '积分管理'
        # 反向取url
        record_url = reverse('stark:web_scorerecord_list', kwargs={'student_id': obj.pk})

        return mark_safe('<a target="_blank" href="%s">%s</a>' % (record_url, obj.score))

    list_display = ['customer', get_another_text('账号/手机号', 'mobile', 'font-weight:bold;'), 'qq', 'emergency_contract', get_m2m_text(
        '已报名班级', 'class_list'), display_score, display_reset_pwd, get_choice_text('状态', 'student_status')]  # 自定义显示

    # def get_list_display(self, request, *args, **kwargs):
    #     """重构：只需要修改按钮"""
    #     value = []
    #     if self.list_display:
    #         value.extend(self.list_display)
    #         value.append(type(self).display_edit)
    #     return value

    def get_urls(self):
        """重构url ，值需要列表功能"""
        patterns = [
            re_path(r'^list/$', self.wrapper(self.changelist_view), name=self.get_list_url_name),
            re_path(r'^change/(?P<pk>\d+)/$', self.wrapper(self.change_view), name=self.get_change_url_name),
            re_path(r'^reset/password/(?P<pk>\d+)/$',
                    self.wrapper(self.reset_password), name=self.get_url_name('reset_pwd')),
        ]

        patterns.extend(self.extra_urls())
        return patterns

    def reset_password(self, request, pk):
        """
        重置密码视图函数
        """
        student_obj = models.Student.objects.filter(pk=pk).first()
        if not student_obj:
            return HttpResponse('该用户不存在，无法重置密码')
        if request.method == 'GET':
            form = ResetPasswordForm()
            return render(request, 'stark/change.html', {'form': form})
        form = ResetPasswordForm(data=request.POST)
        if form.is_valid():
            student_obj.password = form.cleaned_data['password']
            student_obj.save()
            return redirect(self.reverse_list_url())
        return render(request, 'stark/change.html', {'form': form})

    def save(self, request, form, is_update, *args, **kwargs):  # 重写模块中的方法
        print(args, kwargs)
        # user_id = kwargs.get('pk')
        user_id = form.instance.id
        user_mobile = form.cleaned_data['mobile']
        user_obj = models.Student.objects.filter(mobile=user_mobile).exclude(id=user_id).all()
        if user_obj:
            return HttpResponse('该账户/手机号码已存在')
        form.save()


    # 模糊搜索
    search_list = ['customer__name', 'qq', 'mobile', ]
    # 组合搜索
    search_group = [
        Option('class_list', text_func=lambda x: '%s-%s' % (x.school.title, str(x)))  # 利用text_func添加一个lambda函数处理显示字符串
    ]
