# Generated by Django 2.2 on 2020-01-16 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0004_auto_20200116_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orders', models.IntegerField(blank=True, default=0, null=True, verbose_name='排序')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('money', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='打赏金额')),
                ('status', models.BooleanField(default=False, verbose_name='打赏状态')),
                ('trade_no', models.CharField(blank=True, max_length=255, null=True, verbose_name='流水号')),
                ('out_trade_no', models.CharField(blank=True, max_length=255, null=True, verbose_name='支付平台返回的流水号')),
                ('reward_type', models.IntegerField(default=1, verbose_name='打赏类型')),
                ('message', models.TextField(blank=True, null=True, verbose_name='打赏留言')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='article.Article', verbose_name='文章')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '打赏记录',
                'verbose_name_plural': '打赏记录',
                'db_table': 'rr_user_reward',
            },
        ),
    ]
