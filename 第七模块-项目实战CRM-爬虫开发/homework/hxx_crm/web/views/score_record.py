from stark.service.v1 import StarkHandler, StarkModelForm
from django.conf.urls import re_path
from web import models
from .base import PermissionHandler


class ScoreModelForm(StarkModelForm):
    class Meta:
        model = models.ScoreRecord
        fields = ['content', 'score']


class ScoreRecordHandler(PermissionHandler, StarkHandler):
    model_form_class = ScoreModelForm
    list_display = ['content', 'score', 'user', ]  # 自定义显示

    # 重构，url
    def get_urls(self):  # 重写url
        patterns = [
            re_path(r'^list/(?P<student_id>\d+)/$', self.wrapper(self.changelist_view), name=self.get_list_url_name),
            re_path(r'^add/(?P<student_id>\d+)/$', self.wrapper(self.add_view), name=self.get_add_url_name),
        ]

        patterns.extend(self.extra_urls())
        return patterns

    def get_list_display(self, requset, *args, **kwargs):
        """"充定向方法，不显示编辑，删除按钮"""
        value = []
        # 默认展示 修改和 删除
        if self.list_display:
            value.extend(self.list_display)
        return value

    def get_queryset(self, request, *args, **kwargs):
        """筛选对应显示信息"""
        student_id = kwargs.get('student_id')
        return self.model_class.objects.filter(student_id=student_id)

    def save(self, request, form, is_update, *args, **kwargs):
        """保存分数"""
        student_id = kwargs.get('student_id')
        current_user_id = request.session['user_info']['id']
        form.instance.student_id = student_id
        form.instance.user_id = current_user_id
        # 保存积分记录信息
        form.save()
        # 改变学生积分信息
        score = form.instance.score
        # if score > 0:
        #     form.instance.student.score += abs(score)
        # else:
        #     form.instance.student.score -= abs(score)
        # form.instance.student.save()
        student_obj = models.Student.objects.filter(pk=student_id).first()
        student_obj.score += score
        student_obj.save()
