# Generated by Django 3.2 on 2021-10-24 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookie', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user',
            new_name='name',
        ),
    ]
