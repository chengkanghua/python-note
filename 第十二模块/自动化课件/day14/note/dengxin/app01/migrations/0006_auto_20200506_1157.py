# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-05-06 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20200506_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='api_pass_status',
            field=models.IntegerField(choices=[(0, '未通过'), (1, '已通过')], default=0, verbose_name='执行是否通过'),
        ),
        migrations.AlterField(
            model_name='api',
            name='api_run_status',
            field=models.IntegerField(choices=[(0, '未执行'), (1, '已执行')], default=0, verbose_name='是否执行'),
        ),
    ]
