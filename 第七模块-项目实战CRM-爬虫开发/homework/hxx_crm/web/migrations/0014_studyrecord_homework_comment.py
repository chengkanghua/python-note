# Generated by Django 2.2 on 2019-07-26 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_student_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='studyrecord',
            name='homework_comment',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='导师点评'),
        ),
    ]
