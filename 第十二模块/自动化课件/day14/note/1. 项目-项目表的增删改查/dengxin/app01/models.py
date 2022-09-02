from django.db import models

# Create your models here.



class It(models.Model):
    """ 接口项目表 """
    it_name = models.CharField(max_length=32, default='', verbose_name='项目名称')
    it_desc = models.TextField(max_length=255, default='', verbose_name='项目描述')
    it_start_time = models.DateField(verbose_name='项目开始时间')
    it_end_time = models.DateField(verbose_name='项目结束时间')

    def __str__(self):
        return self.it_name


    # class Meta:










