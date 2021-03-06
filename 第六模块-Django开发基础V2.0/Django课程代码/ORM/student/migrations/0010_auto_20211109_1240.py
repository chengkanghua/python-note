# Generated by Django 2.2 on 2021-11-09 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_student_classmate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='student',
            name='chinese_score',
            field=models.IntegerField(default=100, verbose_name='语文分数'),
        ),
        migrations.AlterField(
            model_name='student',
            name='math_score',
            field=models.IntegerField(default=100, verbose_name='数学分数'),
        ),
    ]
