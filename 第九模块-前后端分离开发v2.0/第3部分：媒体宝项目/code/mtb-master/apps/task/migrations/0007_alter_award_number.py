# Generated by Django 3.2 on 2022-04-01 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_rename_good_award_goods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='number',
            field=models.IntegerField(verbose_name='任务数量'),
        ),
    ]
