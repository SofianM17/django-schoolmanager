from django import forms
from .models import *

PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low')
]

class ClassForm(forms.Form):
    name = forms.CharField( max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    time = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Time'}))
    section = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Section'}))
    room = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Room'}), required=False)

class ExamForm(forms.Form): 
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    date = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'Date'}))
    description =  forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    priority = forms.CharField(
        max_length=3,
        widget=forms.Select(choices=PRIORITY_CHOICES),
    )
    time_limit = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Time Limit'}))
    room = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Room'}))
    #username should be taken out as it doesnt make much sense
    username = forms.ModelMultipleChoiceField(queryset=Instructor.objects.all(), widget=forms.TextInput(attrs={'placeholder': 'Username'}))

class HomeworkForm(forms.Form): 
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    date = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'Date'}))
    description =  forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    priority = forms.CharField(
        max_length=3,
        widget=forms.Select(choices=PRIORITY_CHOICES),
    )

    no_questions = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'placeholder': 'No. Questions'}))
    #username should be taken out as it doesnt make much sense
    username = forms.ModelMultipleChoiceField(queryset=Instructor.objects.all(), widget=forms.TextInput(attrs={'placeholder': 'Username'}))

class AssignmentForm(forms.Form): 
    #fields = ('id', 'name', 'date', 'description', 'priority', 'no_questions', 'username')
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    date = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'Date'}))
    description =  forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    priority = forms.CharField(
        max_length=3,
        widget=forms.Select(choices=PRIORITY_CHOICES),
    )
    
    group_members = forms.CharField(max_length = 1000, required=False, widget=forms.TextInput(attrs={'placeholder': 'Group Members'}))
    module = forms.CharField(max_length = 50, required=False, widget=forms.TextInput(attrs={'placeholder': 'Module'}))
    #username should be taken out as it doesnt make much sense
    username = forms.ModelMultipleChoiceField(queryset=Instructor.objects.all(), widget=forms.TextInput(attrs={'placeholder': 'Username'}))