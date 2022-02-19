from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
# Create your models here.

class Food(models.Model):
    title = models.CharField(max_length=32)
    # 不会生成字段，只用于反向查询
    coupons = GenericRelation(to="Coupon")

class Fruit(models.Model):
    title = models.CharField(max_length=32)

class Coupon(models.Model):
    title = models.CharField(max_length=32)

    content_type = models.ForeignKey(to=ContentType,on_delete=None)
    object_id = models.IntegerField()
    content_object = GenericForeignKey("content_type","object_id")
    def __str__(self):
        return self.title
