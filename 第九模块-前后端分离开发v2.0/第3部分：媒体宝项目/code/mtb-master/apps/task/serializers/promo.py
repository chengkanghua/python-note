from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .. import models


class PromoSerializer(serializers.ModelSerializer):
    qr = serializers.SerializerMethodField(read_only=True)
    public_text = serializers.CharField(read_only=True, source="public.nick_name")

    class Meta:
        model = models.Promo
        fields = ['id', 'name', "public", 'public_text', "qr"]

    def get_qr(self, obj):
        # return "http://mtb.pythonav.com{}".format(obj.qr)
        request = self.context['request']
        url = request.build_absolute_uri(obj.qr)
        return url
