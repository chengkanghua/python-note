from django.db import models


class Activity(models.Model):
    """活动表"""
    mtb_user = models.ForeignKey("base.UserInfo", verbose_name="创建人", on_delete=models.CASCADE)
    name = models.CharField(max_length=16, verbose_name="活动名称")
    start_time = models.DateTimeField(verbose_name="活动开始时间")
    end_time = models.DateTimeField(verbose_name="活动结束时间")

    # 开启拉新保护后， 只算扫第一个人的
    # protect_switch = models.SmallIntegerField(verbose_name="拉新保护", choices=((1, "开"), (2, "关"),), default=1)
    protect_switch = models.BooleanField(verbose_name="拉新保护")


class PublicJoinActivity(models.Model):
    """ 参与获得公众号 """
    public = models.ForeignKey("base.PublicNumbers", verbose_name="公众号", on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, verbose_name="活动", on_delete=models.CASCADE, related_name="publics")


class Award(models.Model):
    """ 活动奖励表 """
    activity = models.ForeignKey(Activity, verbose_name="参与活动", on_delete=models.CASCADE, related_name="awards")
    level = models.IntegerField(verbose_name="任务等级", choices=(
        (1, "一阶任务"),
        (2, "二阶任务"),
        (3, "三阶任务"),
    ), default=1)
    count = models.IntegerField(verbose_name="任务数量")
    goods = models.CharField(verbose_name="奖品", max_length=255)


class PosterSetting(models.Model):
    """海报配置表"""
    activity = models.OneToOneField(Activity, verbose_name="活动", on_delete=models.CASCADE, related_name="poster")
    img = models.CharField(verbose_name="背景图片", max_length=128)

    key = models.CharField(verbose_name="海报生成关键字", max_length=10)
    rules = models.CharField(verbose_name="活动规则描述", max_length=256)


class TakePartIn(models.Model):
    """ 参与活动 """
    # activity = models.ForeignKey(Activity, verbose_name="活动", on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, verbose_name="活动", on_delete=models.CASCADE, null=True, blank=True)
    public_number = models.ForeignKey("base.PublicNumbers", verbose_name="公众号", on_delete=models.CASCADE)

    open_id = models.CharField(verbose_name="粉丝OpenID", max_length=64)

    nick_name = models.CharField(verbose_name="粉丝昵称", max_length=64, null=True, blank=True)
    avatar = models.FileField(verbose_name="粉丝头像", null=True, blank=True)

    origin = models.IntegerField(verbose_name="粉丝来源", choices=(
        (0, "其他粉丝"),
        (1, "推广码"),
        (2, "其他")
    ), default=2)

    looking = models.IntegerField(verbose_name="关注状态", choices=(
        (0, "关注中"),
        (1, "已取关"),
    ), default=0)

    part_in = models.IntegerField(verbose_name="参与活动", choices=(
        (0, "参与"),
        (1, "不参与"),  # 助力别人
    ), default=0)

    poster = models.CharField(verbose_name="专属拉新海报", max_length=128, null=True, blank=True)

    black = models.IntegerField(verbose_name="黑名单开关", choices=(
        (0, "未加入黑名单"),
        (1, "加入黑名单"),  # 加入黑名单的人不能参与
    ), default=0)

    level = models.IntegerField(verbose_name="裂变层级", default=1)
    origin_open_id = models.CharField(verbose_name="来源ID", max_length=64, null=True, blank=True)  # 是推广码的ID, 或者是用户的ID

    number = models.IntegerField(verbose_name="邀请人数", default=0)
    task_progress = models.IntegerField(verbose_name="任务完成度", choices=(
        (0, "参与"),
        (1, "完成任务一"),
        (2, "完成任务二"),
        (3, "完成任务三"),
    ), default=0)
    ctime = models.DateTimeField(verbose_name="参与时间", auto_now_add=True)
    subscribe_time = models.DateTimeField(verbose_name="关注时间", null=True, blank=True)


class Promo(models.Model):
    """渠道表"""
    name = models.CharField(verbose_name="渠道名称", max_length=16)
    qr = models.CharField(verbose_name="二维码", max_length=128, null=True, blank=True)
    public = models.ForeignKey("base.PublicNumbers", verbose_name="公众号", on_delete=models.CASCADE)
    mtb_user = models.ForeignKey("base.UserInfo", verbose_name="创建人", on_delete=models.CASCADE)
