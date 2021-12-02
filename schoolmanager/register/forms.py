from django import forms as f
from django.contrib.auth import login, authenticate
from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    ACCOUNT_TYPE_CHOICES = [
    ('Student', 'Student'),
    ('Instructor', 'Instructor'),
    ]
    account_type = f.ChoiceField(choices = ACCOUNT_TYPE_CHOICES)
    school = f.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "school", "account_type"]