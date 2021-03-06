# Generated by Django 3.2 on 2022-03-31 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_publicnumbers'),
        ('msg', '0006_auto_20220331_0105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='标题')),
                ('template_id', models.CharField(blank=True, max_length=128, null=True, verbose_name='模板ID')),
                ('content', models.TextField(blank=True, null=True, verbose_name='发送内容')),
                ('exec_date', models.DateTimeField(verbose_name='执行时间')),
                ('task_id', models.CharField(max_length=64, verbose_name='Celery任务ID')),
                ('status', models.IntegerField(choices=[(1, '待发送'), (2, '发送中'), (3, '已完成')], default=1, verbose_name='任务状态')),
                ('count', models.IntegerField(blank=True, default=0, verbose_name='发送数量')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('mtb_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.userinfo', verbose_name='创建者')),
                ('public', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.publicnumbers', verbose_name='公众号')),
            ],
        ),
    ]
