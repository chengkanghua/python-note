# Generated by Django 3.2 on 2021-10-09 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20211008_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='description',
            field=models.TextField(default='', verbose_name='个性签名'),
        ),
    ]
