from django.db import models

class Permission(models.Model):
    """
    权限表
    """
    title = models.CharField(verbose_name='标题', max_length=32)
    url = models.CharField(verbose_name='含正则的URL', max_length=128)

    def __str__(self):
        return self.title


class Role(models.Model):
    """
    角色
    blank=True ，该字段允许为空 注意，这与 null 不同。 null 纯属数据库相关，而 blank 则与验证相关。如果一个字段有 blank=True，表单验证将允许输入一个空值。如果一个字段有 blank=False，则该字段为必填字段。
    """
    title = models.CharField(verbose_name='角色名称', max_length=32)
    permissions = models.ManyToManyField(verbose_name='拥有的所有权限', to='Permission', blank=True)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """
    用户表
    """
    name = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    email = models.CharField(verbose_name='邮箱', max_length=32)
    roles = models.ManyToManyField(verbose_name='拥有的所有角色', to='Role', blank=True)

    def __str__(self):
        return self.name
