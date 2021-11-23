from django import forms
from django.db.models.base import Model
from .models import *
from django.forms import ModelForm

class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = '__all__'

class ClubForm(ModelForm):
    class Meta:
        model = Club
        fields = '__all__'

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'

class HomeworkForm(ModelForm):
        class Meta:
            model = Homework
            fields = '__all__'

class AssignmentForm(ModelForm):
        class Meta:
            model = Assignment
            fields = '__all__'

class ExamPrepForm(ModelForm):
        class Meta:
            model = ExamPrep
            fields = '__all__'

class FinanceForm(ModelForm):
        class Meta:
            model = Finance
            fields = '__all__'
