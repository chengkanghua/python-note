# Generated by Django 3.2 on 2021-10-08 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='姓名')),
                ('age', models.SmallIntegerField(default=18, verbose_name='年龄')),
                ('sex', models.SmallIntegerField(choices=[(0, '女'), (1, '男'), (2, '保密')])),
                ('birthday', models.DateField()),
            ],
            options={
                'db_table': 'db_student',
            },
        ),
    ]
