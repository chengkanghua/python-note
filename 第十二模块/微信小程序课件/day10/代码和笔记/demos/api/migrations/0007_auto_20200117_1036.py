# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-01-17 02:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200116_0907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, '在职'), (2, '离职')], verbose_name='状态')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('cover', models.CharField(max_length=128, verbose_name='封面')),
            ],
        ),
        migrations.CreateModel(
            name='Depart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标签')),
            ],
        ),
        migrations.AddField(
            model_name='auction',
            name='dp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Depart', verbose_name='部门'),
        ),
        migrations.AddField(
            model_name='auction',
            name='tags',
            field=models.ManyToManyField(to='api.Tag', verbose_name='标签'),
        ),
    ]
