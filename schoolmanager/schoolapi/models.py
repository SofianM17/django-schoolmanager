from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class User (models.Model):
    username = models.CharField(max_length=50)
    school = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.username)

    class Meta:
        abstract = True

class Student(User):
    program = models.CharField(max_length=50)

class Instructor(User):
    faculty = models.CharField(max_length=50)

class Class(models.Model):
    name = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    room = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return '%s' % (self.name)

class Club(models.Model):
    username = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    meeting_time = models.DateTimeField(blank=True)

    def __str__(self):
        return '%s' % (self.name)
    
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
    username = models.ForeignKey(Student, on_delete=models.CASCADE)
    
class Task(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField()
    description = models.CharField(max_length=1000, blank=True)
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low')
    ]
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    username = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.ForeignKey(Class, on_delete=models.CASCADE)

    class Meta:
        abstract=True

class Exam(Task):
    time_limit = models.IntegerField()
    room = models.CharField(max_length=50)
    username = models.ForeignKey(Instructor, on_delete=models.CASCADE)

class Homework(Task):
    no_questions = models.IntegerField(blank=True)
    username = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.name)

class Assignment(Task):
    group_members = models.CharField(max_length = 1000, blank = True)
    module = models.CharField(max_length = 50, blank = True)
    username = models.ForeignKey(Instructor, on_delete=models.CASCADE)

class ExamPrep(models.Model):
    name = models.ForeignKey(Exam, on_delete=models.CASCADE)
    PREP_CHOICES = [
        ('prac_exam', 'Practice Exam'),
        ('review_sess', 'Review Session'),
        ('prep_event', 'Exam Prep Event')
    ]
    prep_type = models.CharField(max_length = 100, choices = PREP_CHOICES)
    
class Finance(models.Model):
    initialBudget = models.FloatField()
    income = models.FloatField()
    tuition = models.FloatField()
    equipment = models.CharField(max_length = 1000, blank = True)
    books = models.CharField(max_length = 1000, blank = True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)