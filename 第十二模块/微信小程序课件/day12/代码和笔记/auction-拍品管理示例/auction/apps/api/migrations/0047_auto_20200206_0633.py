# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-02-06 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0046_auto_20200206_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionitem',
            name='cover',
            field=models.FileField(max_length=128, upload_to='', verbose_name='拍品封面'),
        ),
    ]
