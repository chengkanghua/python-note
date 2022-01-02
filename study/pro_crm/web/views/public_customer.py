from stark.service.v1 import StarkHandler, get_m2m_text, get_choice_text, StarkModelForm
from web import models
from django.db import transaction
from django.conf.urls import url
from django.utils.safestring import mark_safe
from django.shortcuts import HttpResponse, render,redirect


class PublicCustomerModelForm(StarkModelForm):
    class Meta:
        model = models.Customer
        exclude = ['consultant', ]  # 公户排除录入课程顾问字段


class PublicCustomerHandler(StarkHandler):

    def display_record(self, obj=None, is_header=None):
        if is_header:
            return '跟进记录'
        record_url = self.reverse_commons_url(self.get_url_name('record_view'), pk=obj.pk)
        return mark_safe('<a href="%s">查看跟进</a>' % record_url)

    list_display = [StarkHandler.display_checkbox, 'name', 'qq', get_m2m_text('咨询课程', 'course'), display_record,
                    get_choice_text('状态', 'status')]

    def get_queryset(self, request, *args, **kwargs):
        return self.model_class.objects.filter(consultant__isnull=True)

    model_form_class = PublicCustomerModelForm

    def extra_urls(self):
        patterns = [
            url(r'^record/(?P<pk>\d+)/$', self.wrapper(self.record_view),
                name=self.get_url_name('record_view')),
        ]
        return patterns

    def record_view(self, request, pk):
        """
        查看跟进记录的视图
        :param request:
        :param pk:
        :return:
        """
        # return HttpResponse('跟进记录')
        record_list = models.ConsultRecord.objects.filter(customer_id=pk)
        return render(request, 'record_view.html', {'record_list': record_list})

    def action_multi_apply(self, request, *args, **kwargs):
        '''
        批量申请到私户
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''

        current_user_id = request.session['user_info']['id']
        pk_list = request.POST.getlist('pk')
        private_customer_count = models.Customer.objects.filter(consultant=current_user_id,status=2).count()

        # 私户个数限制
        if (private_customer_count + len(pk_list)) > models.Customer.MAX_PRIVATE_CUSTOMER_COUNT:
            return HttpResponse('做人不能太贪心,私户中已有%s个客户, 最多只能申请%s' %(private_customer_count,models.Customer.MAX_PRIVATE_CUSTOMER_COUNT - private_customer_count))

        # 数据库中加锁
        flag =False
        with transaction.atomic(): # 事务
            # 在数据中加锁
            origin_queryset = models.Customer.objects.filter(id__in=pk_list,status=2,consultant__isnull=True).select_for_update()
            if len(origin_queryset) == len(pk_list): # 加锁的数量和申请的数据不一致的话,说明其中有已经被申请走了.
                models.Customer.objects.filter(id__in=pk_list,status=2,consultant__isnull=True).update(consultant_id=current_user_id)
                flag = True
        if not flag:
            return HttpResponse('手速太慢了, 选中的客户已经被其他人申请, 请重新选择')

    action_multi_apply.text = "申请到我的私户"
    action_list = [action_multi_apply,]
