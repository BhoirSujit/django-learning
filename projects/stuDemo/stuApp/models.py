from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    email = models.EmailField(blank=True)
    gender = models.CharField(choices=[('male', 'Male'), ('female', 'Female')])
    std = models.CharField(default="9")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True) 




