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
    response = requests.get('http://'+request.get_host()+'/api/class/')
    classes = response.json()

    return render(request, "schoolapi/dashboard.html", {"classes" : classes})

# Class CRUD
def addClass(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            requests.post('http://'+request.get_host()+'/api/class/', form)
        return HttpResponseRedirect("/")
            
    else:
        form = ClassForm()
            
    return render(request, 'schoolapi/addClass.html', {'form': form})

def deleteClass(request, id):
    if request.method == 'POST':
        requests.delete('http://'+request.get_host()+'/api/class/'+id+'/')
        return HttpResponseRedirect("/")
    return render(request, "schoolapi/delete_view.html", {})

def updateClass(request, id):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            requests.put('http://'+request.get_host()+'/api/class/'+id+'/', form)
        return HttpResponseRedirect("/")
    else:
        form_fields_req = requests.get('http://'+request.get_host()+'/api/class/'+id+'/')
        form_fields = form_fields_req.json()
        form = ClassForm(initial={"name": form_fields['name'], "time": form_fields['time'],
        "section": form_fields['section'], "room": form_fields['room']})
            
    return render(request, 'schoolapi/updateClass.html', {'form': form})

# Exam CRUD
def addExam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            requests.post('http://'+request.get_host()+'/api/exam/', form)
        return HttpResponseRedirect("/")
            
    else:
        form = ExamForm()
            
    return render(request, 'schoolapi/addExam.html', {'form': form})