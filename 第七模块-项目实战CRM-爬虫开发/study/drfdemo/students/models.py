from django.db import models

# Create your models here.
class Student(models.Model):
    # 表字段声明
    # 字段名=models.数据类型(字段约束)
    name = models.CharField(null=False, max_length=32, verbose_name="姓名")
    sex  = models.BooleanField(default=True, verbose_name="性别")
    age  = models.IntegerField(verbose_name="年龄")
    class_num = models.CharField(max_length=5, verbose_name="班级编号")
    description = models.TextField(max_length=1000, verbose_name="个性签名")

    # 表信息
    class Meta:
        # 设置表名
        db_table="tb_students"
        verbose_name="学生"
        verbose_name_plural=verbose_name

    # 模型的操作方法
    def __str__(self):
        return self.name