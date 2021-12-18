from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User, UserManager, AbstractUser
from django.contrib.auth import get_user_model
User = get_user_model()
from register.models import CustomUser

# Create your models here.
TYPE_CHOICES = [
    ('Network', 'Networking'),
    ('InfoSess', 'Information Session'),
    ('Speaker', 'Career Fair'),
    ('Party', 'Party'),
    ('Workshop', 'Workshop'),
    ('Sports', 'Sports'),
    ('Conference', 'Conference'),
    ('Other', 'Other'),
] 

#class User (models.Model):
#    username = models.CharField(max_length=50)
#    school = models.CharField(max_length=50)

#    def __str__(self):
#        return '%s' % (self.username)

#    class Meta:
#        abstract = True

class Class(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    time = models.TimeField(max_length=50)
    section = models.CharField(max_length=50)
    room = models.CharField(max_length=50, blank=True)


    def __str__(self):
        return '%s' % (self.name)

class Club(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    meeting_time = models.TimeField(max_length=50, blank=True)

    def __str__(self):
        return '%s' % (self.name)

   
class Event(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    date = models.DateField(max_length=50)
    description = models.CharField(max_length = 1000, blank=True)
    host = models.CharField(max_length=50, blank=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    
PRIORITY_CHOICES = [
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low')
]
class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    className = models.ForeignKey(Class, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=50)
    date = models.DateField()
    description = models.CharField(max_length=1000, blank=True)
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)

    class Meta:
        abstract=True

    def __str__(self):
        return self.task_name

class Exam(Task):
    start_time = models.TimeField(max_length=50)
    room = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.task_name)

class Homework(Task):
    no_questions = models.IntegerField(blank=True)

    def __str__(self):
        return '%s' % (self.task_name)

class Assignment(Task):
    group_members = models.CharField(max_length = 1000, blank = True)
    module = models.CharField(max_length = 50, blank = True)

class ExamPrep(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    PREP_CHOICES = [
        ('Practice Exam', 'Practice Exam'),
        ('Review Session', 'Review Session'),
        ('Exam Prep Event', 'Exam Prep Event'),
        ('Other', 'Other')
    ]
    prep_type = models.CharField(max_length = 100, choices = PREP_CHOICES)
    
class Finance(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    initialBudget = models.FloatField()
    income = models.FloatField()
    tuition = models.FloatField()
    equipment = models.FloatField()
    books = models.FloatField()

    @property
    def total(self):
        return self.initialBudget + self.income - self.tuition - self.equipment - self.books

    #student = models.OneToOneField(Student, on_delete=models.CASCADE)

# class customUser(AbstractUser):
#     acc_types = (
#         ('Student', 'Student'),
#         ('Instructor', 'Instructor')
#     )
#     user_type = models.CharField(max_length=2,
#                                  choices=acc_types)

# class UserDetails(models.Model):
#     type = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
#     extra_info = models.CharField(max_length=200)