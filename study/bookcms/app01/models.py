from django.db import models


# Create your models here.

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32,unique=True)
    pub_date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    author = models.CharField(max_length=32)
    publish = models.CharField(max_length=32)

class user(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=32)