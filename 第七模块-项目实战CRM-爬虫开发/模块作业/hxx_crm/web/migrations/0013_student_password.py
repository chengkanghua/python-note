# Generated by Django 2.2 on 2019-07-12 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_auto_20190628_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=64, null=True, verbose_name='密码'),
        ),
    ]
