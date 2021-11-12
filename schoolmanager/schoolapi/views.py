from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Student, Instructor, Event, Club
from .serializers import UserSerializer

# Create your views here.

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer 