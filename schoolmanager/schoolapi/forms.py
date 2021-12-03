from typing import Text
from django import forms
from django.db.models.base import Model
from django.db.models.fields import DateField
from django.forms.widgets import CheckboxSelectMultiple, ChoiceWidget, NumberInput, Select, SelectMultiple
from .models import *
from django.forms import ModelForm, TextInput
from django.contrib.admin import widgets

class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Name'
                }),
            'time': widgets.AdminTimeWidget(attrs={
                'placeholder': 'hh:mm:ss'
                }),
            'section': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Section'
                }),
            'room': TextInput(attrs={
                'class': "form-control", 
                'placeholder': 'Room'
                })
        }

class ClubForm(ModelForm):
    class Meta:
        model = Club
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Name'
                }),
            'meeting_time': widgets.AdminTimeWidget(attrs={
                'placeholder': 'hh:mm:ss'
                })
        }
        labels = {
            "name" : "Club Name",
            "meeting_time" : "Club Name",
        }

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Name'
                }),
            'date': widgets.AdminDateWidget(attrs={
                'placeholder': 'Date'
                }),
            'description': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Description'
                }),
            'host': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Host'
                }),
            'type': Select(attrs={
                'class': "form-control"
                }),
            'club': Select(attrs={
                'class': "form-control"
                })
        }
        labels = {
            "name" : "Event Name",
            "type" : "Event Type",
        }

class ExamForm(ModelForm):
    date = forms.DateField(widget=widgets.AdminDateWidget(attrs={
                'placeholder': 'yyyy-mm-dd'
                }))
    class Meta:
        model = Exam
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'className': Select(attrs={
                'class': "form-control"
                }),
            'description': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Description'
                }),
            'priority': Select(attrs={
                'class': "form-control"
                }),
            'start_time': widgets.AdminTimeWidget(attrs={
                'placeholder': 'hh:mm:ss'
                }),
            'room': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Room'
                })
        }
        labels = {
            "className" : "Class",
            "start_time" : "Start Time"
        }

class HomeworkForm(ModelForm):
    class Meta:
        model = Homework
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'className': Select(attrs={
                'class': "form-control"
                }),
            'date': widgets.AdminDateWidget(attrs={
                'placeholder': 'yyyy-mm-dd'
                }),
            'description': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Description'
                }),
            'priority': Select(attrs={
                'class': "form-control"
                }),
            'no_questions': NumberInput(attrs={
                'class': "form-control",
                'placeholder': '# questions'
                })
        }
        labels = {
            "className" : "Class",
            "no_questions": 'Number of Questions',
            "date": 'Due Date'
        }

class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'className': Select(attrs={
                'class': "form-control"
                }),
            'date': widgets.AdminDateWidget(attrs={
                'placeholder': 'yyyy-mm-dd'
                }),
            'description': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Description'
                }),
            'priority': Select(attrs={
                'class': "form-control"
                }),
            'group_members': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Group members'
                }),
            'module': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Module'
                }),
        }
        labels = {
            "className" : "Class",
            "group_members": 'Group Members',
            "date": 'Due Date'
        }

class ExamPrepForm(ModelForm):
    class Meta:
        model = ExamPrep
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'exam': Select(attrs={
                'class': "form-control"
                }),
            'prep_type': Select(attrs={
                'class': "form-control"
                })
        }

class FinanceForm(ModelForm):
    class Meta:
        model = Finance
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'initialBudget': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Initial budget'
                }),
            'income': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Income'
                }),
            'tuition': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Tuition'
                }),
            'equipment': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Equipment'
                }),
            'books': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Books'
                })
        }