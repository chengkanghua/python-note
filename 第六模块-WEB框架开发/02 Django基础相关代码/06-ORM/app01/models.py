from django.db import models


# Create your models here.

class Book(models.Model):    # 类必须继承 models.Model
    id = models.AutoField(primary_key=True)  # 自增长 加主键
    title = models.CharField(max_length=32, unique=True)  # 最大的长度, 唯一值
    pub_date = models.DateField()  # 时间日期
    price = models.DecimalField(max_digits=8, decimal_places=2)  # 这是最大的数 999999.99
    publish = models.CharField(max_length=32)  # 字符串 最大长度32

    def __str__(self):
        return self.title
