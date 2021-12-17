from typing import Text
from django import forms
from django.db.models.base import Model
from django.db.models.fields import DateField
from django.forms.widgets import CheckboxSelectMultiple, ChoiceWidget, NumberInput, Select, SelectMultiple
from .models import *
from django.forms import ModelForm, TextInput
from django.contrib.admin import widgets
from django.contrib.auth import get_user_model
User = get_user_model()

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
            "meeting_time" : "Meeting Time",
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
                'placeholder': 'yyyy-mm-dd'
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
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['club'].queryset = Club.objects.filter(user=user)

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
            'task_name': TextInput(attrs={
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
            "start_time" : "Start Time",
            "task_name" : "Exam Name",
        }
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['className'].queryset = Class.objects.filter(user=user)

class HomeworkForm(ModelForm):
    class Meta:
        model = Homework
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'className': Select(attrs={
                'class': "form-control"
                }),
            'task_name': TextInput(attrs={
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
            "task_name" : "Homework Name",
            "no_questions": 'Number of Questions',
            "date": 'Due Date'
        }
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['className'].queryset = Class.objects.filter(user=user)

class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'className': Select(attrs={
                'class': "form-control"
                }),
            'task_name': TextInput(attrs={
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
            "date": 'Due Date',
            "task_name" : "Assignment Name",
        }
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['className'].queryset = Class.objects.filter(user=user)

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
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['exam'].queryset = Exam.objects.filter(user=user)

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

class FinancePosForm(ModelForm):
    class Meta:
        model = Finance
        fields = ('initialBudget', 'income')
        exclude = ('user',)
        widgets = {
            'initialBudget': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Initial budget'
                }),
            'income': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Income'
                })
        }

class FinanceNegForm(ModelForm):
    class Meta:
        model = Finance
        fields = ('tuition', 'equipment', 'books')
        exclude = ('user',)
        widgets = {
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