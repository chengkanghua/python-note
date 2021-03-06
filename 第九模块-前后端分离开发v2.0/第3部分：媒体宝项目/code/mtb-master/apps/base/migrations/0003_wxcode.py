# Generated by Django 3.2 on 2022-03-26 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20220319_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='WxCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_type', models.IntegerField(verbose_name='类型')),
                ('value', models.CharField(max_length=128, verbose_name='值')),
                ('period', models.PositiveIntegerField(verbose_name='过期时间')),
            ],
        ),
    ]
