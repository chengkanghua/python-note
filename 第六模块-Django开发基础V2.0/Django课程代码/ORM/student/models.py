from django.db import models

# Create your models here.
'''

-- auto-generated definition
create table db_student
(
    id       int auto_increment primary key,
    name     varchar(32) not null,
    age      smallint(6) not null,
    sex      smallint(6) not null,
    birthday date        not null,
    constraint name
        unique (name)
);

'''


class Student(models.Model):
    sex_choices = (
        (0, "女"),
        (1, "男"),
        (2, "保密"),
    )

    # id = models.AutoField(primary_key=True)   # 这个不写会自动创建
    name = models.CharField(max_length=32, unique=True, verbose_name="姓名")
    age = models.SmallIntegerField(verbose_name="年龄",default=18)
    sex = models.SmallIntegerField(choices=sex_choices)  # choices值从sex_choices里选择
    birthday = models.DateField(verbose_name='生日')

    classmate = models.CharField(max_length=32,verbose_name="班级" ,default="python脱产12期")

    description = models.TextField(null=True,verbose_name="个性签名")

    chinese_score = models.IntegerField(default=100,verbose_name='语文分数')
    math_score = models.IntegerField(default=100,verbose_name='数学分数')

    class Meta:   # 数据库表名默认是 项目名_Student, 以下是修改了这个表名为db_student
        db_table = "db_student"

    def __str__(self):
        return self.name



