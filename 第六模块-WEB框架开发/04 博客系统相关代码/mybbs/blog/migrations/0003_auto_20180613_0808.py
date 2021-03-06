# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-13 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180521_1229'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterModelOptions(
            name='article2tag',
            options={'verbose_name': '文章-标签', 'verbose_name_plural': '文章-标签'},
        ),
        migrations.AlterModelOptions(
            name='articledetail',
            options={'verbose_name': '文章详情', 'verbose_name_plural': '文章详情'},
        ),
        migrations.AlterModelOptions(
            name='articleupdown',
            options={'verbose_name': '点赞', 'verbose_name_plural': '点赞'},
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': '博客', 'verbose_name_plural': '博客'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '文章分类', 'verbose_name_plural': '文章分类'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '评论', 'verbose_name_plural': '评论'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '标签', 'verbose_name_plural': '标签'},
        ),
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
        migrations.RemoveField(
            model_name='blog',
            name='site',
        ),
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
