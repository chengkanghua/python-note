from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .. import models


class ActivityListSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()

    class Meta:
        model = models.Activity
        fields = ['id','name', "img"]

    def get_img(self, obj):
        # print(obj.poster.img)
        return "http://mtb.pythonav.com{}".format(obj.poster.img)


class ActivitySerializer(serializers.ModelSerializer):
    date_range = serializers.ListField()

    class Meta:
        model = models.Activity
        fields = ['name', 'date_range', 'protect_switch']

    def validate_date_range(self, attrs):
        # print("时间范围", attrs)
        # raise ValidationError("公众号选择错误")
        return attrs


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Award
        fields = ['level', 'count', 'goods']


class PosterSettingSerialize(serializers.ModelSerializer):
    class Meta:
        model = models.PosterSetting
        fields = ['key', 'rules', 'img']
