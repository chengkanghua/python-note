from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.activity import ActivitySerializer, AwardSerializer, PosterSettingSerialize, ActivityListSerializer
from utils import return_code
from apps.base import models as base_models
from .. import models

from utils.ext.mixins import MtbCreateModelMixin, MtbListModelMixin, MtbDestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from utils.ext.filters import SelfFilterBackend
from rest_framework.filters import BaseFilterBackend


class CustomSearch(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        search_map = {"public": "publics__public_id", "name": "name__contains"}
        condition = {}
        for k, v in search_map.items():
            # ?name=t&public=4
            data = request.query_params.get(k)
            if not data:
                continue
            condition[v] = data
        if condition:
            queryset = queryset.filter(**condition)
        return queryset


class ActivityView(MtbCreateModelMixin, MtbListModelMixin, MtbDestroyModelMixin, GenericViewSet):
    filter_backends = [SelfFilterBackend, CustomSearch, ]

    queryset = models.Activity.objects.all().order_by('-id')
    serializer_class = ActivityListSerializer

    def create(self, request, *args, **kwargs):
        user_id = request.user.user_id
        # 1.接收数据
        # print(request.data)
        # 2.分别校验 活动表/公众号/奖励/海报
        # 2.1 活动相关
        ser = ActivitySerializer(data=request.data)
        if not ser.is_valid():
            return Response({"code": return_code.ERROR, 'detail': "活动数据格式错误"})
        # 2.2 公众号，当前已登录用户是否有权限操作公众
        public_list = request.data.get("publicList")
        if not public_list:
            return Response({"code": return_code.ERROR, 'detail': "公众号设置错误"})
        db_public_list_count = base_models.PublicNumbers.objects.filter(mtb_user_id=user_id, id__in=public_list).count()
        if len(public_list) != db_public_list_count:
            return Response({"code": return_code.ERROR, 'detail': "公众号设置错误"})

        # 2.3 奖励
        # [{'level': 1, 'count': 10, 'goods': ''}, {'level': 2, 'count': 20, 'goods': ''}, {'level': , 'count': 30, 'goods': ''}]
        award_list = request.data.get("awardList")
        if not award_list:
            return Response({"code": return_code.ERROR, 'detail': "奖励设置错误"})
        ser_award = AwardSerializer(data=award_list, many=True)
        if not ser_award.is_valid():
            print(ser_award.errors)
            return Response({"code": return_code.ERROR, 'detail': "奖励设置错误"})

        # 2.4 海报设置
        ser_img = PosterSettingSerialize(data=request.data)
        if not ser_img.is_valid():
            return Response({"code": return_code.ERROR, 'detail': "海报设置错误"})

        start_time, end_time = ser.validated_data.pop("date_range")
        instance = ser.save(start_time=start_time, end_time=end_time, mtb_user_id=request.user.user_id)
        obj_list = []
        for item in public_list:
            obj = models.PublicJoinActivity(activity=instance, public_id=item)
            obj_list.append(obj)
        models.PublicJoinActivity.objects.bulk_create(obj_list)
        ser_award.save(activity=instance)
        ser_img.save(activity=instance)

        # 3.在数据库新增
        return Response({"code": return_code.SUCCESS})
