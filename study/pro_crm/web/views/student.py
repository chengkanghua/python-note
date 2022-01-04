from django.conf.urls import url
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.shortcuts import render,HttpResponse,redirect
from stark.service.v1 import StarkHandler,get_choice_text,get_m2m_text,StarkModelForm,Option,get_another_text
from .base import PermissionHandler
from web.forms.student import StudentModelForm, ResetPasswordForm
from web import models

# class StudentModelForm(StarkModelForm):
#     class Meta:
#         model = models.Student
#         fields = ['qq','mobile','emergency_contract','memo']


class StudnetHandler(PermissionHandler,StarkHandler):
    model_form_class = StudentModelForm
    def display_reset_pwd(self, obj=None, is_header=None):
        if is_header:
            return "重置密码"
        reset_url = self.reverse_commons_url(self.get_url_name('reset_pwd'), pk=obj.pk)
        return mark_safe('<a href="%s">重置密码</a>' % reset_url)

    def display_score(self,obj=None,is_header=None,*args,**kwargs):
        if is_header:
            return '积分管理'
        record_url = reverse('stark:web_scorerecord_list',kwargs={'student_id':obj.pk})
        return mark_safe('<a target="_blank" href="%s">%s</a>' % (record_url,obj.score))
    list_display = ['customer',get_another_text('账号/手机号','mobile'),'qq','emergency_contract',get_m2m_text('已报班级','class_list'),
                    display_score,display_reset_pwd,
                    get_choice_text('状态','student_status')]

    def get_add_btn(self, request, *args, **kwargs):
        return None

    def get_list_display(self,request,*args,**kwargs):
        value = []
        if self.list_display:
            value.extend(self.list_display)
            value.append(type(self).display_edit)
        return value

    def get_urls(self):
        patterns = [
            url(r'^list/$',self.wrapper(self.changelist_view),name=self.get_list_url_name),
            url(r'^change/(?P<pk>\d+)/$',self.wrapper(self.change_view),name=self.get_change_url_name),
            url(r'^reset/password/(?P<pk>\d+)/$',
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
    search_list = ['customer__name','qq','mobile',]
    # 组合搜索
    search_group = [
        Option('class_list',text_func=lambda x: '%s-%s' % (x.school.title,str(x)))
    ]