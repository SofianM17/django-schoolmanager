from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterForm(UserCreationForm):
    # ACCOUNT_TYPE_CHOICES = [
    # ('Student', 'Student'),
    # ('Instructor', 'Instructor'),
    # ]
    # account_type = f.ChoiceField(choices = ACCOUNT_TYPE_CHOICES)
    school = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "school", "is_student", "is_instructor")
        labels = {
            "is_student": "Student",
            "is_instructor": "Instructor"
        }

# class RegisterForm(UserCreationForm):
#     username = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     password1 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )

#     class Meta:
#         model = User
#         fields = ('username', 'password1', 'password2', 'is_student', 'is_instructor')

# class LoginForm(UserCreationForm):

#     class Meta:
#         model = User
#         fields = ("username", "password1", "is_student", "is_instructor")

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )