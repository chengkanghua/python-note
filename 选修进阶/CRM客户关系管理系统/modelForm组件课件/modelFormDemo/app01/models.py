from django.db import models

# Create your models here.





class Student(models.Model):

    name = models.CharField(max_length=5)
    age = models.IntegerField()
    birth = models.DateField()
    email = models.EmailField()
    createDate = models.DateField(auto_now_add=True)


