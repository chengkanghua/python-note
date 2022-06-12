import os
import requests
from utils.token import get_authorizer_access_token
from django.conf import settings
from utils.ext.mixins import MtbCreateModelMixin, MtbDestroyModelMixin, MtbUpdateModelMixin, MtbListModelMixin
from rest_framework.viewsets import GenericViewSet
from utils.ext.filters import SelfFilterBackend
from ..serializers.promo import PromoSerializer
from .. import models

from utils.ext.page import MtbPageNumberPagination
from utils.ext.mixins import MtbPageNumberListModelMixin
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet, filters


class PromoFilterSet(FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='contains')
    public = filters.NumberFilter(field_name='public_id')

    class Meta:
        model = models.Promo
        fields = ["name", "public"]


class PromoView(MtbCreateModelMixin, MtbPageNumberListModelMixin, MtbDestroyModelMixin, MtbUpdateModelMixin,
                GenericViewSet):
    filter_backends = [SelfFilterBackend, DjangoFilterBackend]
    filterset_class = PromoFilterSet
    pagination_class = MtbPageNumberPagination

    queryset = models.Promo.objects.all().order_by('-id')
    serializer_class = PromoSerializer

    def perform_create(self, serializer):
        mtb_user_id = self.request.user.user_id

        # 1.创建渠道数据
        instance = serializer.save(mtb_user_id=mtb_user_id)

        # 2.生成永久二维码
        access_token = get_authorizer_access_token(instance.public)
        qr_res = requests.post(
            url="https://api.weixin.qq.com/cgi-bin/qrcode/create",
            params={
                "access_token": access_token
            },
            json={
                "action_name": "QR_LIMIT_STR_SCENE",
                "action_info": {
                    "scene": {
                        "scene_str": "2_{}".format(instance.id)  # 自定义字段，客户扫码后，自动携带（助力用）
                    }
                }
            }
        )
        qr_data_dict = qr_res.json()
        qr_content = requests.get(
            "https://mp.weixin.qq.com/cgi-bin/showqrcode",
            params={"ticket": qr_data_dict["ticket"]}
        ).content

        # 3.写入本地
        local_qr_folder = os.path.join(settings.MEDIA_ROOT, "qr")
        if not os.path.exists(local_qr_folder):
            os.makedirs(local_qr_folder)
        local_qr_path = os.path.join(local_qr_folder, "{}.png".format(instance.id))
        with open(local_qr_path, mode='wb') as f:
            f.write(qr_content)

        # 4.构造Media URL写入数据库
        # https://www.xxx.com/media/qr/1.png
        qr_image_url = "{}qr/{}.png".format(settings.MEDIA_URL, instance.id)
        instance.qr = qr_image_url
        instance.save()


class TotalPromoView(MtbListModelMixin, GenericViewSet):
    filter_backends = [SelfFilterBackend, ]
    queryset = models.Promo.objects.all().order_by('-id')
    serializer_class = PromoSerializer
