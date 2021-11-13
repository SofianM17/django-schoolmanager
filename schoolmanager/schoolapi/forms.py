from django import forms

class ClassForm(forms.Form):
    name = forms.CharField(max_length=50, label='Name')
    time = forms.CharField(label='Time')
    section = forms.CharField(max_length=50, label='Section')
    room = forms.CharField(max_length=50, label='Room', required=False)