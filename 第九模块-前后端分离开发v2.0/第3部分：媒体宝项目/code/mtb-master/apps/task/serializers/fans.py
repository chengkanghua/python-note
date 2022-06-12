from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .. import models


class FansSerializer(serializers.ModelSerializer):
    looking_text = serializers.CharField(source="get_looking_display")
    task_progress = serializers.CharField(source="get_task_progress_display")

    class Meta:
        model = models.TakePartIn
        fields = ['id', 'nick_name', 'open_id', 'looking', "looking_text", "number", "task_progress"]
