# Generated by Django 2.0.1 on 2021-10-18 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20211018_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=32),
        ),
    ]
