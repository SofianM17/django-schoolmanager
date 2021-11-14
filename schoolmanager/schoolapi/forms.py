from django import forms

class ClassForm(forms.Form):
    name = forms.CharField( max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    time = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Time'}))
    section = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Section'}))
    room = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Room'}), required=False)