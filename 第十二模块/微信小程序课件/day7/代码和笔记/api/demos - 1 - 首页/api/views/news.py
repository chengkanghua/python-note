from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView
from api import models

from django.forms import model_to_dict


class NewsModelSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    topic = serializers.SerializerMethodField()

    class Meta:
        model = models.News
        fields = ['id', 'cover', 'content', 'topic', "user", 'favor_count']

    def get_user(self, obj):
        return model_to_dict(obj.user, fields=['id', 'nickname', 'avatar'])

    def get_topic(self, obj):
        if not obj.topic:
            return
        return model_to_dict(obj.topic, fields=['id', 'title'])


"""
class NewsView(APIView):
    def get(self,request,*args,**kwargs):
        min_id = request.query_params.get('min_id')
        max_id = request.query_params.get('max_id')
        if min_id:
            queryset = models.News.objects.filter(id__lt=min_id).order_by('-id')[0:10]
        elif max_id:
            queryset = models.News.objects.filter(id__gt=max_id).order_by('id')[0:10]
        else:
            queryset = models.News.objects.all().order_by('-id')[0:10]
        ser = NewsModelSerializer(instance=queryset,many=True)
        return Response(ser.data,status=200)
"""
# ############################# 动态列表 #############################
from utils.filters import MaxFilterBackend, MinFilterBackend
from utils.pagination import OldBoyLimitPagination


class NewsView(ListAPIView):
    serializer_class = NewsModelSerializer
    queryset = models.News.objects.all().order_by('-id')

    pagination_class = OldBoyLimitPagination
    filter_backends = [MinFilterBackend, MaxFilterBackend]


# ############################# 话题  #############################
class TopicModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Topic
        fields = "__all__"


class TopicView(ListAPIView):
    serializer_class = TopicModelSerializer
    queryset = models.Topic.objects.all().order_by('-id')

    pagination_class = OldBoyLimitPagination
    filter_backends = [MinFilterBackend, MaxFilterBackend]
