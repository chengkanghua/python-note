from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
class User(AbstractUser):
    """用户模型类"""
    nickname = models.CharField(max_length=20, null=True, blank=True, verbose_name="用户昵称")
    avatar = models.ImageField(upload_to="avatar", null=True, blank=True, verbose_name="用户头像")
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    money = models.DecimalField(max_digits=7, decimal_places=2, default=0, verbose_name="账户余额")
    blocked_money = models.DecimalField(max_digits=7, decimal_places=2, default=0, verbose_name="冻结余额")

    class Meta:
        db_table = 'rr_users'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

from renranapi.utils.models import BaseModel
class Record(BaseModel):
    """收支记录"""
    TYPE_CHOICES = (
        (0, "赞赏"),
        (1, "购买"),
        (2, "提现"),
        (3, "充值"),
        (4, "其他"),
    )
    STAUTS_CHOICES = (
        (0, "未支付"),
        (1, "已支付"),
    )
    GOODS_CHOICES = (
        (0, "其他"),
        (1, "文章"),
    )
    types = models.IntegerField(choices=TYPE_CHOICES, default=4, verbose_name="类型")
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="record_list", verbose_name="用户")
    money = models.DecimalField(decimal_places=2, max_digits=8, default=0, verbose_name="金额")
    status = models.IntegerField(choices=STAUTS_CHOICES, default=0, verbose_name="状态")
    goods = models.CharField(max_length=150, verbose_name="物品名称")
    goods_id = models.IntegerField(default=0, verbose_name="物品名称")
    goods_type = models.IntegerField(choices=GOODS_CHOICES, default=0,verbose_name="物品类型")
    other_user = models.IntegerField(default=0, verbose_name="用户")

    class Meta:
        db_table = "rr_user_record"
        verbose_name = '用户收支记录'
        verbose_name_plural = verbose_name

    @property
    def goods_type_text(self):
        return self.get_goods_type_display()

    @property
    def types_text(self):
        return self.get_types_display()

    @property
    def other_user_name(self):
        if self.other_user>0:
            try:
                other_user_obj = User.objects.get(pk=self.other_user)
                return other_user_obj.nickname
            except User.DoesNotExist:
                return ""

    @property
    def status_text(self):
        return self.get_status_display()