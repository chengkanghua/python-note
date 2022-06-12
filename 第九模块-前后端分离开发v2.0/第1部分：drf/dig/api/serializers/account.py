from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from api import models


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(label="确认密码", min_length=8, write_only=True)
    password = serializers.CharField(label="密码", min_length=8, write_only=True)

    class Meta:
        model = models.UserInfo
        fields = ['username', "phone", "password", "confirm_password"]

    def validate_username(self, value):
        exists = models.UserInfo.objects.filter(username=value, deleted=False).exists()
        if exists:
            raise ValidationError("用户名已存在")
        return value

    def validate_phone(self, value):
        exists = models.UserInfo.objects.filter(phone=value, deleted=False).exists()
        if exists:
            raise ValidationError("手机号已存在")
        return value

    def validate_confirm_password(self, value):
        password = self.initial_data.get('password')
        if password == value:
            return value
        raise ValidationError("两次密码不一致")


class AuthSerializer(serializers.Serializer):
    username = serializers.CharField(label="用户名", write_only=True, required=False)  # 不提交
    phone = serializers.CharField(label="手机", write_only=True, required=False)  # 不提交
    password = serializers.CharField(label="密码", min_length=8, write_only=True)

    def validate_username(self, value):
        username = self.initial_data.get("username")
        phone = self.initial_data.get("phone")
        if not username and not phone:
            raise ValidationError("用户名或手机为空")
        if username and phone:
            raise ValidationError("提交数据异常")
        return value
