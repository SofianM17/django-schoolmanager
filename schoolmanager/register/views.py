from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            return redirect("/login")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form":form})

def acc_type(response):
    return render(response, "register/acc_type.html", {})

def login(response):
    if response.method == "POST":
        form = LoginForm(response.POST)
        if form.is_valid():
            form.save()
            user = authenticate()
        # if user is not None and user.is_student:
        #     login(response, user)
        #     return redirect("student")
        # elif user is not None and user.is_instructor:
        #     login(response, user)
        #     return redirect("instructor")
    return render(response, "login.html", {"form":form})

def logout(response):
    logout(response)
    return redirect('/login')
