from django.db import models
from django.contrib.auth.models import User, UserManager, AbstractUser

class CustomUser(AbstractUser):
    # acc_types = (
    #     ('Student', 'Student'),
    #     ('Instructor', 'Instructor')
    # )
    # user_type = models.CharField(max_length=20, choices=acc_types)
  
    school = models.CharField(max_length=50)

    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.username)

# class UserDetails(models.Model):
#     type = models.OneToOneField('CustomUser', on_delete=models.CASCADE)

# class Student(models.Model):
#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE
#     )
#     school = models.CharField(max_length=50)
#     program = models.CharField(max_length=50)
#     #objects = UserManager()

# class Instructor(models.Model):
#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE
#     )
#     school = models.CharField(max_length=50)
#     faculty = models.CharField(max_length=50)
#     #objects = UserManager()