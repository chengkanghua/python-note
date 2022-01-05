from django.utils.safestring import mark_safe
from django.shortcuts import render, HttpResponse
from django.urls import re_path
from stark.service.v1 import StarkHandler, StarkModelForm, get_choice_text, get_m2m_text
from web import models
from .base import PermissionHandler

class PublicCustomerModelForm(StarkModelForm):
    class Meta:
        model = models.Customer
        exclude = ['consultant', ]


class PublicCustomerHandler(PermissionHandler, StarkHandler):

    # 增加一个 查看记录按钮
    def display_record(self, obj=None, is_header=None, *args, **kwargs):
        if is_header:
            return '跟进记录'
        record_url = self.reverse_common_url(
            self.get_url_name('record_view'), pk=obj.pk)
        return mark_safe('<a href="%s">查看跟进</a>' % record_url)

    list_display = [StarkHandler.display_checkbox, 'name', 'qq', get_choice_text('状态', 'status'),
                    get_m2m_text('咨询课程', 'course'), display_record]

    # 自定义筛选：过滤只显示未被分配的客户
    def get_queryset(self, request, *args, **kwargs):
        return self.model_class.objects.filter(consultant__isnull=True)

    model_form_class = PublicCustomerModelForm

    # 增加一个url（跟进记录）用写好的钩子方法
    def extra_urls(self):
        patterns = [
            re_path(r'^record/(?P<pk>\d+)$', self.wrapper(self.record_view),
                    name=self.get_url_name('record_view'))
        ]
        return patterns

    def record_view(self, request, pk):
        """
        跟进记录视图
        """
        record_list = models.ConsultRecord.objects.filter(customer=pk)
        return render(request, 'record_view.html', {'record_list': record_list})

    # 自定义函数,重写父类中方法
    def action_multi_apply(self, request, *args, **kwargs):
        """批量申请到私户，自定义函数"""
        pk_list = request.POST.getlist('pk')  # 选中客户id列表
        current_user_id = request.session['user_info']['id']
        # 状态验证未成交 且 没有课程顾问的
        private_customer_count = models.Customer.objects.filter(consultant_id=current_user_id,
                                                                status=2).count()  # 取当前用户的私户个数
        if (private_customer_count + len(pk_list)) > 150:
            return HttpResponse('私户中总个数已经有%s 人，还能申请%s 个' % (
                private_customer_count, models.Customer.MAX_PRIVATE_CUSTOMER - private_customer_count))

        # 如果多个人同时提交申请私户可能会有bug 【数据库加锁，许可证】
        from django.db import transaction

        flag = False
        with transaction.atomic():  # 事务
            # 上锁  select * from customer where id in [11,22] for update;
            origin_queryset = models.Customer.objects.filter(
                id__in=pk_list, status=2, consultant__isnull=True).select_for_update()

            if len(origin_queryset) == len(pk_list):
                models.Customer.objects.filter(id__in=pk_list, status=2, consultant__isnull=True).update(
                    consultant_id=current_user_id)
                flag = True

        if not flag:
            return HttpResponse('选中的客户已经被其他人申请走了')

    action_multi_apply.text = '批量申请到私户'

    action_list = [action_multi_apply, ]
