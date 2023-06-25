from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    roll=models.IntegerField()
    department=models.CharField(max_length=50, default='Computer Science')
    semester=models.IntegerField(default='1')
    total=models.IntegerField(default='0')
    earned=models.IntegerField(default='0')
    sgpa=models.FloatField(default='0')
    result_status=models.CharField(max_length=10)