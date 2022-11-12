from django.db import models


class School(models.Model):
    """
    校区表
    如：
        北京昌平校区
        上海浦东校区
        深圳南山校区
    """
    title = models.CharField(verbose_name='校区名称', max_length=32)

    def __str__(self):
        return self.title


class Department(models.Model):
    """
    部门表
    """
    title = models.CharField(verbose_name='部门名称', max_length=16)

    def __str__(self):
        return self.title
