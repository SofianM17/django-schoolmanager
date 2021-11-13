from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
import requests
from .forms import *
from django.http import HttpResponseRedirect

# Create your views here.

# API
class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class InstructorView(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    
class ClassView(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class ClubView(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class ExamView(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class HomeworkView(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer

class AssignmentView(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class ExamPrepView(viewsets.ModelViewSet):
    queryset = ExamPrep.objects.all()
    serializer_class = ExamPrepSerializer

# FRONT END
def dashboard(request):
    response = requests.get('http://127.0.0.1:8000/api/class/')
    classes = response.json()

    return render(request, "schoolapi/dashboard.html", {"classes" : classes})

def addClass(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            requests.post('http://127.0.0.1:8000/api/class/', form)
        return HttpResponseRedirect("/")
            
    else:
        form = ClassForm()
            
    return render(request, 'schoolapi/addClass.html', {'form': form})