from django.db import models
from django.contrib.auth.models import User, UserManager, AbstractUser

class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    school = models.CharField(max_length=50)
    program = models.CharField(max_length=50)
    #objects = UserManager()

class Instructor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    school = models.CharField(max_length=50)
    faculty = models.CharField(max_length=50)
    #objects = UserManager()