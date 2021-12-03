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
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Name'
                }),
            'meeting_time': TextInput(attrs={
                'class': "form-control", 
                'placeholder': 'Meeting Time'
                })
        }

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Name'
                }),
            'date': TextInput(attrs={
                'class': "form-control", 
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

class ExamForm(ModelForm):
    date = forms.DateField(widget=widgets.AdminDateWidget(attrs={
                'placeholder': 'yyyy-dd-mm'
                }))
    class Meta:
        model = Exam
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'cName': Select(attrs={
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
            "cName" : "Class",
            "start_time" : "Start Time"
        }

class HomeworkForm(ModelForm):
    class Meta:
        model = Homework
        fields = '__all__'
        widgets = {
            'name': Select(attrs={
                'class': "form-control"
                }),
            'date': TextInput(attrs={
                'class': "form-control", 
                'placeholder': 'Date'
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

class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'
        widgets = {
            'name': Select(attrs={
                'class': "form-control"
                }),
            'date': TextInput(attrs={
                'class': "form-control", 
                'placeholder': 'Date'
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

class ExamPrepForm(ModelForm):
    class Meta:
        model = ExamPrep
        fields = '__all__'
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