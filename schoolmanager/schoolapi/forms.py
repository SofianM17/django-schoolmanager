from django import forms
from .models import *

class ClassForm(forms.Form):
    name = forms.CharField( max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    time = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Time'}))
    section = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Section'}))
    room = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Room'}), required=False)

class ExamForm(forms.Form):
    username = forms.ModelChoiceField(queryset = Student.objects.all())
    name = forms.ModelChoiceField(queryset = Class.objects.all())
    date = forms.CharField( max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Date'}))
    description = forms.CharField( max_length=1000, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    priority = forms.CharField( label='Priority', widget=forms.Select(choices=PRIORITY_CHOICES))
    time_limit = forms.CharField( max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Time limit'}))
    room = forms.CharField( max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Room'}))

class HomeworkForm(forms.Form):
    name = forms.ModelChoiceField(queryset = Class.objects.all())
    date = forms.CharField( max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Date'}))
    description = forms.CharField( max_length=1000, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    priority = forms.CharField( label='Priority', widget=forms.Select(choices=PRIORITY_CHOICES))
    no_questions = forms.CharField( max_length=50, widget=forms.TextInput(attrs={'placeholder': '#'}))
    username = forms.ModelChoiceField(queryset = Student.objects.all())

class AssignmentForm(forms.Form):
    name = forms.ModelChoiceField(queryset = Class.objects.all())
    date = forms.CharField( max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Date'}))
    description = forms.CharField( max_length=1000, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    priority = forms.CharField( label='Priority', widget=forms.Select(choices=PRIORITY_CHOICES))
    group_members = forms.CharField( max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Group members'}))
    module = forms.CharField( max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Module'}))
    username = forms.ModelChoiceField(queryset = Student.objects.all())
