from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    school = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % (self.username)

class Student(models.Model):
    program = models.CharField(max_length=50)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

class Instructor(models.Model):
    faculty = models.CharField(max_length=50)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

class Club(models.Model):
    name = models.CharField(max_length=50)
    meeting_time = models.DateTimeField(blank=True)
    
class Event(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField()
    description = models.CharField(max_length = 1000, blank=True)
    host = models.CharField(max_length=50, blank=True)
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
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)