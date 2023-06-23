from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    roll=models.IntegerField()
    #department=models.CharField(max_length=50)
    result_status=models.CharField(max_length=10)