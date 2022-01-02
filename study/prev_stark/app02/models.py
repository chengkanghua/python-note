from django.db import models

# Create your models here.
'''
主机表
    主机名
    ip
角色
    角色名称    
'''
class Host(models.Model):
    host = models.CharField(verbose_name='主机名',max_length=32)
    ip   = models.GenericIPAddressField(verbose_name='ip')

class Role(models.Model):
    title = models.CharField(verbose_name='角色名称',max_length=32)







