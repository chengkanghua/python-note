from django.db import models


# Create your models here.


# 作者表
class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()


# 出版社表
class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()


# 图书表
class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    publishDate = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)  # 最大值999.99

    # 与Publish建立一对多的关系,外键字段建立在多的一方 django会自动生成publish_id字段
    publish = models.ForeignKey(to="Publish", to_field="nid", on_delete=models.CASCADE)
    # 与Author表建立多对多的关系,ManyToManyField可以建在两个模型中的任意一个，自动创建第三张表
    # 自动建立第三张表 book_authors
    authors = models.ManyToManyField(to='Author', )
