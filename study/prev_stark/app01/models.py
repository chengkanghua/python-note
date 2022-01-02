from django.db import models

# Create your models here.

'''
部门表
    部门名称
用户表
    姓名
    年龄
    email
    depart 部门外键
'''
class Depart(models.Model):
    title = models.CharField(verbose_name='部门名称',max_length=32)

class UserInfo(models.Model):
    name = models.CharField(verbose_name='姓名',max_length=32)
    age = models.CharField(verbose_name='年龄',max_length=32)
    email = models.CharField(verbose_name='邮箱',max_length=32)
    depart = models.ForeignKey(verbose_name='部门',to='Depart',on_delete=models.CASCADE)