# Generated by Django 3.2 on 2021-10-11 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20211011_0437'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='classAddr',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='classTime',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='credit',
            field=models.IntegerField(default=3, verbose_name='学分'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
