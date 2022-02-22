from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Food,Coupon
from django.contrib.contenttypes.models import ContentType
# Create your views here.

class DemoView(APIView):
    def get(self,request):
        food_obj = Food.objects.filter(id=1).first()
        # Coupon.objects.create(title="双十一面包九折促销", content_object=food_obj)

        # 查询面包有哪些优惠
        coupons = food_obj.coupons.all()
        # print(coupons)
        # for title in coupons:
        #     print(title)

        # 优惠券查对象
        coupon_obj = Coupon.objects.filter(id=1).first()
        content_obj = coupon_obj.content_object
        # print(content_obj.title,coupon_obj.title)

        # 通过ContentType 表找表模型
        content = ContentType.objects.filter(app_label="demo",model="food").first()
        print(content)
        model_class = content.model_class()
        ret = model_class.objects.all()
        print(ret)
        return Response("ContentType测试")