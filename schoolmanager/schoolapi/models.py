from django.db import models
from django.db.models.fields import CharField

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
    meeting_time = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return '%s' % (self.name)

   
class Event(models.Model):
    name = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    description = models.CharField(max_length = 1000, blank=True)
    host = models.CharField(max_length=50, blank=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    username = models.ForeignKey(Student, on_delete=models.CASCADE)
    
PRIORITY_CHOICES = [
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low')
]
class Task(models.Model):
    username = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.CharField(max_length=50)
    description = models.CharField(max_length=1000, blank=True)
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)

    class Meta:
        abstract=True

    def name_name(self):
        return self.name.name

class Exam(Task):
    time_limit = models.CharField(max_length=50)
    room = models.CharField(max_length=50)

class Homework(Task):
    no_questions = models.IntegerField(blank=True)

    def __str__(self):
        return '%s' % (self.name)

class Assignment(Task):
    group_members = models.CharField(max_length = 1000, blank = True)
    module = models.CharField(max_length = 50, blank = True)

class ExamPrep(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
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