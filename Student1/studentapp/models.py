from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    usertype=models.CharField(max_length=50)

class Student(models.Model):
    student_id=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()
    guardian=models.CharField(max_length=20)

class Teacher(models.Model):
    teacher_id=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()
    salary=models.IntegerField()
    experience=models.IntegerField()


