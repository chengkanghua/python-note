from django.db import models

# Create your models here.


# 作者表   name age
class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age  = models.IntegerField()

# 出版社  name city email
class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()

# 图书表  title publishDate  price     一对多外键对出版社id   多对多 第三张表对作者表
class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    publishDate = models.DateField()
    price = models.DecimalField(max_digits=5,decimal_places=2)

    publish = models.ForeignKey(to="Publish", on_delete=models.CASCADE)

    authors = models.ManyToManyField(to="Author")
