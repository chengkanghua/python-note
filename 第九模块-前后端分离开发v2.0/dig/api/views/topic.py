from rest_framework.viewsets import GenericViewSet
from django_filters import FilterSet, filters
from django_filters.rest_framework import DjangoFilterBackend

from api import models
from api.serializers.topic import TopicSerializer
from api.extension.filter import SelfFilterBackend
from api.extension.mixins import DigCreateModelMixin, DigListModelMixin, DigDestroyModelMixin, DigUpdateModelMixin


class TopicFilterSet(FilterSet):
    # ?latest_id=99             ->  id<99
    # ?latest_id=99&limit=10    ->  id<99  limit 10
    latest_id = filters.NumberFilter(field_name='id', lookup_expr='lt')

    class Meta:
        model = models.Topic
        fields = ["latest_id", ]


class TopicView(DigListModelMixin, DigCreateModelMixin, DigDestroyModelMixin, DigUpdateModelMixin, GenericViewSet):
    """ 主题 """

    # 当前登录用户的调教
    filter_backends = [SelfFilterBackend, DjangoFilterBackend]
    filterset_class = TopicFilterSet

    queryset = models.Topic.objects.filter(deleted=False).order_by('-id')

    serializer_class = TopicSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()
