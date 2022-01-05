from django.utils.safestring import mark_safe
from django.shortcuts import reverse
from stark.service.v1 import StarkHandler, StarkModelForm, get_m2m_text, get_choice_text
from web import models
from .base import PermissionHandler

class PrivateCustomerModelForm(StarkModelForm):
    class Meta:
        model = models.Customer
        exclude = ['consultant', ]


class PrivateCustomerHandler(PermissionHandler, StarkHandler):

    def display_record(self, obj=None, is_header=None, *args, **kwargs):
        if is_header:
            return '跟进记录'
        # 直接用 reverse，不用加原搜索条件保留
        record_url = reverse('stark:web_consultrecord_list', kwargs={'customer_id': obj.pk})  # 带上id 反向生成别名
        return mark_safe('<a target="_blank" href="%s">跟进</a>' % record_url)

    def display_pay_record(self, obj=None, is_header=None, *args, **kwargs):
        if is_header:
            return '缴费记录'
        # 直接用 reverse，不用加原搜索条件保留
        record_url = reverse('stark:web_paymentrecord_list', kwargs={'customer_id': obj.pk})  # 带上id 反向生成别名
        return mark_safe('<a target="_blank" href="%s">缴费</a>' % record_url)

    list_display = [StarkHandler.display_checkbox, 'name', 'qq',
                    get_m2m_text('咨询课程', 'course'), get_choice_text(
                        '状态', 'status'), display_record, display_pay_record]  # 自定义显示

    # 自定义筛选：过滤只显示自己的私人客户
    def get_queryset(self, request, *args, **kwargs):
        current_user_id = request.session['user_info']['id']
        return self.model_class.objects.filter(consultant_id=current_user_id)

    model_form_class = PrivateCustomerModelForm

    def save(self, request, form, is_update, *args, **kwargs):  # 重写模块中的方法
        """当在销售顾问登录的情况下，可以添加咨询客户，默认就是添加给自己"""
        # 默认添加学员是给当前id的销售顾问
        if not is_update:  # 新增操作
            current_user_id = request.session['user_info']['id']
            form.instance.consultant_id = current_user_id
        form.save()  # 保存

        # 自定义函数,重写父类中方法

    def action_multi_remove(self, request, *args, **kwargs):
        """批量申请到私户，自定义函数"""
        pk_list = request.POST.getlist('pk')  # 选中客户id列表
        current_user_id = request.session['user_info']['id']
        # 当前课程顾问必须是自己
        self.model_class.objects.filter(id__in=pk_list, consultant_id=current_user_id).update(consultant_id=None)

    action_multi_remove.text = '批量剔除到公户'

    action_list = [action_multi_remove, ]
