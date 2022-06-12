import time
import datetime
import json
import requests
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from utils.ext.mixins import MtbCreateModelMixin, MtbDestroyModelMixin
from utils import return_code
from utils.token import get_authorizer_access_token
from utils.ext.filters import SelfFilterBackend
from ..serializers.message import ServiceMessageSerializer, TemplateMessageSerializer, MessageSerializer
from ..serializers.message import TemplateSopSerializer, SopSerializer
from .. import models
from .. import tasks
from mtb import celery_app
from celery.result import AsyncResult


class ServiceMessageView(MtbCreateModelMixin, GenericViewSet):
    """ 客服消息接口 """
    queryset = models.Message.objects.order_by("-id")
    serializer_class = ServiceMessageSerializer

    def perform_create(self, serializer):
        """ 序列化：对请求的数据校验成功后，执行保存。"""
        mtb_user_id = self.request.user.user_id
        public_object = serializer.validated_data["public"]

        # 1.校验图片和文本，至少选择一项
        content = serializer.validated_data["content"]
        img = serializer.validated_data["img"]  # media/upload/xxxx/xxx/xxx.png
        if not content and not img:
            serializer._errors['content'] = ["文本和图片至少选择一项", ]
            return Response({"code": return_code.FIELD_ERROR, 'detail': serializer.errors})

        # 2. 如果有图片，上传图片到微信的素材库
        media_id = None
        if img:
            authorizer_access_token = get_authorizer_access_token(public_object)
            # 调用微信接口
            res = requests.post(
                url="https://api.weixin.qq.com/cgi-bin/material/add_material",
                params={
                    "access_token": authorizer_access_token,
                    "type": "image"
                },
                files={
                    "media": (
                        'message-{}-{}.png'.format(public_object.authorizer_app_id, int(time.time() * 1000)),
                        open(img[1:], mode='rb'),
                        "image/png"
                    )
                },
            )
            media_id = res.json()['media_id']

        # 3.数据库中新建记录
        instance = serializer.save(
            mtb_user_id=mtb_user_id,
            msg_type=2,
            media_id=media_id
        )

        # 4.创建celery任务获得任务ID
        task_id = tasks.send_service_message.delay(instance.pk, public_object.authorizer_app_id).id
        instance.task_id = task_id
        instance.save()


class TemplateMessageView(MtbCreateModelMixin, GenericViewSet):
    """ 模板消息接口 """
    queryset = models.Message.objects.order_by("-id")
    serializer_class = TemplateMessageSerializer

    def perform_create(self, serializer):
        mtb_user_id = self.request.user.user_id
        public_object = serializer.validated_data["public"]

        """
        {
            title: "",
            public: "",
            template_id: "", // 模板ID iPk5sOIt5X_flOVKn5GrTFpncEYTojx6ddbt8WYoV5s
            interaction: 1,

           
        },
        
         template_item_dict = {
            "result":"", 
            "withdrawMoney":"", ....
        }
        """
        template_item_dict = serializer.validated_data.pop("templateItemDict")

        # 数据库创建
        instance = serializer.save(
            msg_type=1,
            mtb_user_id=mtb_user_id,
            content=json.dumps(template_item_dict)
        )
        # Celery
        task_id = tasks.send_template_message.delay(instance.pk, public_object.authorizer_app_id, template_item_dict).id
        instance.task_id = task_id
        instance.save()


from utils.ext.page import MtbPageNumberPagination
from utils.ext.mixins import MtbPageNumberListModelMixin
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet, filters


class MessageFilterSet(FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='contains')
    interaction = filters.NumberFilter(field_name='interaction')
    public = filters.NumberFilter(field_name='public_id')

    class Meta:
        model = models.Message
        fields = ["title", "interaction", "public"]


# ?page=1
# ?title=ffffff&public=4&interaction=1   pip install django-filter==21.1
# 分页：limit offset
class MessageView(MtbPageNumberListModelMixin, MtbDestroyModelMixin, GenericViewSet):
    filter_backends = [SelfFilterBackend, DjangoFilterBackend]
    filterset_class = MessageFilterSet

    queryset = models.Message.objects.order_by("-id")
    serializer_class = MessageSerializer

    pagination_class = MtbPageNumberPagination

    def perform_destroy(self, instance):
        if instance.status == 2:
            # task = AsyncResult(id=instance.task_id, app=celery_app)
            # task.revoke(terminate=True)
            return Response({"code": return_code.ERROR, "detail": "正在发送中，无法删除"})
        if instance.status == 1:
            # 取消celery任务
            task = AsyncResult(id=instance.task_id, app=celery_app)
            task.revoke()

        instance.delete()


class TemplateSopView(MtbCreateModelMixin, GenericViewSet):
    """ SOP模板消息接口 """
    queryset = models.Sop.objects.order_by("-id")
    serializer_class = TemplateSopSerializer

    def perform_create(self, serializer):
        mtb_user_id = self.request.user.user_id
        public_object = serializer.validated_data["public"]
        template_item_dict = serializer.validated_data.pop("templateItemDict")

        # 数据库创建
        instance = serializer.save(
            mtb_user_id=mtb_user_id,
            content=json.dumps(template_item_dict)
        )

        # Celery定时任务（定时任务）
        # - 1.django时间配置成本地时间 settings.py
        # - 2.celery去执行某个任务（在某个时刻）- 只认utc时间
        # - 3.执行任务
        #         tasks.函数.delay(参数..)
        #         tasks.函数.apply_async(args=[参数...],eta=执行任务的UTC时间)
        utc_datetime = datetime.datetime.utcfromtimestamp(instance.exec_date.timestamp())

        task_id = tasks.send_template_sop.apply_async(
            args=[instance.id, public_object.authorizer_app_id, template_item_dict], eta=utc_datetime).id
        instance.task_id = task_id
        instance.save()


class SopFilterSet(FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='contains')
    public = filters.NumberFilter(field_name='public_id')

    class Meta:
        model = models.Sop
        fields = ["title", "public"]


class SopView(MtbPageNumberListModelMixin, MtbDestroyModelMixin, GenericViewSet):
    filter_backends = [SelfFilterBackend, DjangoFilterBackend]
    filterset_class = SopFilterSet

    queryset = models.Sop.objects.order_by("-id")
    serializer_class = SopSerializer

    pagination_class = MtbPageNumberPagination

    def perform_destroy(self, instance):
        if instance.status == 2:
            # task = AsyncResult(id=instance.task_id, app=celery_app)
            # task.revoke(terminate=True)
            return Response({"code": return_code.ERROR, "detail": "正在发送中，无法删除"})
        if instance.status == 1:
            # 取消celery任务
            task = AsyncResult(id=instance.task_id, app=celery_app)
            task.revoke()

        instance.delete()
