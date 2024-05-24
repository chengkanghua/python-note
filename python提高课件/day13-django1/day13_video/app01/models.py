from django.db import models


class Administrator(models.Model):
    """ 管理员表 """
    type_choices = (
        (1, "管理员"),
        (2, "超级管理员"),
    )
    user_type = models.SmallIntegerField(verbose_name="用户类型", choices=type_choices, default=1)

    username = models.CharField(verbose_name="用户名", max_length=32, db_index=True)
    password = models.CharField(verbose_name="密码", max_length=64)
    mobile = models.CharField(verbose_name="手机号", max_length=11, null=True, blank=True, db_index=True)

    # true,激活
    # false，已删除
    active = models.BooleanField(verbose_name="是否激活", default=True, help_text="False表示删除")


class Customer(models.Model):
    """ 客户 """
    username = models.CharField(verbose_name="用户名", max_length=32, db_index=True)
    password = models.CharField(verbose_name="密码", max_length=64)
    balance = models.DecimalField(verbose_name="账户余额", default=0, max_digits=10, decimal_places=2)

    creator = models.ForeignKey(verbose_name="创建者", to="Administrator", on_delete=models.CASCADE)
    create_date = models.DateTimeField(verbose_name="创建日期", auto_now_add=True)
    active = models.BooleanField(verbose_name="是否激活", default=True, help_text="False表示删除")


class ChargeRecord(models.Model):
    """ 充值记录 """
    amount = models.DecimalField(verbose_name="充值金额", default=0, max_digits=10, decimal_places=2)
    customer = models.ForeignKey(verbose_name="客户", to="Customer", on_delete=models.CASCADE)
    creator = models.ForeignKey(verbose_name="管理员", to="Administrator", on_delete=models.CASCADE)
    create_date = models.DateTimeField(verbose_name="充值时间", auto_now_add=True)


class PricePolicy(models.Model):
    """ 价格策略
    10000    5
    20000    9
    30000    13
    """
    count = models.IntegerField(verbose_name="数量")
    price = models.DecimalField(verbose_name="价格", default=0, max_digits=10, decimal_places=2)


class Order(models.Model):
    """ 订单，创建好之后放在redis的队列中（生产者 & 消费者） """
    status_choices = (
        (1, "待执行"),
        (2, "正在执行"),
        (3, "已完成"),
        (4, "失败"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=1)

    oid = models.CharField(verbose_name="订单号", max_length=64, help_text="用户ID+时间戳", unique=True)
    url = models.URLField(verbose_name="视频地址")

    # 疑问，FK和PricePolicy关联是不是会更好？
    count = models.IntegerField(verbose_name="数量")
    price = models.DecimalField(verbose_name="价格", default=0, max_digits=10, decimal_places=2)

    old_view_count = models.IntegerField(verbose_name="原播放量", default=0)

    customer = models.ForeignKey(verbose_name="客户", to="Customer", on_delete=models.CASCADE)
    memo = models.TextField(verbose_name="备注", null=True, blank=True)
