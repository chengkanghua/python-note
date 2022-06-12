from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .. import models


class ServiceMessageSerializer(serializers.ModelSerializer):
    """ 客服消息 """

    class Meta:
        model = models.Message
        fields = ['title', 'public', "content", 'img']

    def validate_public(self, obj):
        request = self.context['request']

        if obj.mtb_user_id == request.user.user_id:
            return obj
        raise ValidationError("公众号选择错误")


class TemplateMessageSerializer(serializers.ModelSerializer):
    templateItemDict = serializers.JSONField(write_only=True)

    class Meta:
        model = models.Message
        fields = ['title', 'public', "interaction", "template_id", "templateItemDict"]


class MessageSerializer(serializers.ModelSerializer):
    public_text = serializers.CharField(source="public.nick_name")
    interaction_text = serializers.CharField(source="get_interaction_display")
    msg_type_text = serializers.CharField(source="get_msg_type_display")
    status_text = serializers.CharField(source="get_status_display")

    class Meta:
        model = models.Message
        fields = ['id', 'title', "count", "public_text", 'status', "status_text", "interaction_text", "msg_type_text"]


class TemplateSopSerializer(serializers.ModelSerializer):
    templateItemDict = serializers.JSONField(write_only=True)

    class Meta:
        model = models.Sop
        fields = ['title', 'public', "exec_date", "template_id", "templateItemDict"]


class SopSerializer(serializers.ModelSerializer):
    public_text = serializers.CharField(source="public.nick_name")
    status_text = serializers.CharField(source="get_status_display")
    exec_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = models.Sop
        fields = ['id', 'title', "count", "public_text", 'status', "status_text", "exec_date"]
