# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-05-06 03:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20200506_0943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_name', models.CharField(default='', max_length=32, verbose_name='用例名称')),
                ('api_desc', models.CharField(default='', max_length=32, verbose_name='用例描述')),
                ('api_url', models.CharField(default='', max_length=32, verbose_name='请求URL')),
                ('api_method', models.CharField(default='', max_length=32, verbose_name='请求类型')),
                ('api_params', models.CharField(default={}, max_length=32, verbose_name='请求参数')),
                ('api_data', models.CharField(default={}, max_length=32, verbose_name='请求data')),
                ('api_expect', models.CharField(default={}, max_length=32, verbose_name='预期结果')),
                ('api_report', models.TextField(verbose_name='报告')),
                ('api_run_time', models.DateTimeField(default='', verbose_name='执行时间')),
                ('api_pass_status', models.DateTimeField(choices=[(0, '未通过'), (1, '已通过')], verbose_name='执行是否通过')),
                ('api_run_status', models.DateTimeField(choices=[(0, '未执行'), (1, '已执行')], verbose_name='是否执行')),
                ('api_sub_it', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.It', verbose_name='所属接口项目')),
            ],
        ),
    ]
