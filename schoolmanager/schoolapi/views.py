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

class FinanceView(viewsets.ModelViewSet):
    queryset = Finance.objects.all()
    serializer_class = FinanceSerializer

# FRONT END
def dashboard(request):
    response = requests.get('http://'+request.get_host()+'/api/class/')
    classes = response.json()

    response = requests.get('http://'+request.get_host()+'/api/exams/')
    exams = response.json()

    response = requests.get('http://'+request.get_host()+'/api/homework/')
    homework = response.json()

    response = requests.get('http://'+request.get_host()+'/api/assignment/')
    assignments = response.json()

    return render(request, "schoolapi/dashboard.html", {"classes" : classes, 
    "exams" : exams, "homework" : homework, "assignments" : assignments})

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
            
    return render(request, 'schoolapi/forms.html', {'form': form})

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
            
    return render(request, 'schoolapi/forms.html', {'form': form})

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
            
    return render(request, 'schoolapi/forms.html', {'form': form})

def deleteExam(request, id):
    if request.method == 'POST':
        requests.delete('http://'+request.get_host()+'/api/exams/'+id+'/')
        return HttpResponseRedirect("/")
    return render(request, "schoolapi/delete_view.html", {})

def updateExam(request, id):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            requests.put('http://'+request.get_host()+'/api/exam/'+id+'/', form)
        return HttpResponseRedirect("/")
    else:
        form_fields_req = requests.get('http://'+request.get_host()+'/api/class/'+id+'/')
        form_fields = form_fields_req.json()
        form = ExamForm(initial={})
            
    return render(request, 'schoolapi/forms.html', {'form': form})

 # Homework CRUD
def addHomework(request):
    if request.method == 'POST':
        form = HomeworkForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            requests.post('http://'+request.get_host()+'/api/homework/', form)
        return HttpResponseRedirect("/")
            
    else:
        form = HomeworkForm()
            
    return render(request, 'schoolapi/forms.html', {'form': form})

def deleteHomework(request, id):
    if request.method == 'POST':
        requests.delete('http://'+request.get_host()+'/api/homework/'+id+'/')
        return HttpResponseRedirect("/")
    return render(request, "schoolapi/delete_view.html", {})

def updateHomework(request, id):
    if request.method == 'POST':
        form = HomeworkForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            requests.put('http://'+request.get_host()+'/api/homework/'+id+'/', form)
        return HttpResponseRedirect("/")
    else:
        form_fields_req = requests.get('http://'+request.get_host()+'/api/class/'+id+'/')
        form_fields = form_fields_req.json()
        form = HomeworkForm(initial={})
            
    return render(request, 'schoolapi/forms.html', {'form': form})

# Assignment CRUD
def addAssignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            requests.post('http://'+request.get_host()+'/api/assignment/', form)
        return HttpResponseRedirect("/")
            
    else:
        form = AssignmentForm()
            
    return render(request, 'schoolapi/forms.html', {'form': form})

def deleteAssignment(request, id):
    if request.method == 'POST':
        requests.delete('http://'+request.get_host()+'/api/assignment/'+id+'/')
        return HttpResponseRedirect("/")
    return render(request, "schoolapi/delete_view.html", {})

def updateAssignment(request, id):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            requests.put('http://'+request.get_host()+'/api/assignment/'+id+'/', form)
        return HttpResponseRedirect("/")
    else:
        form_fields_req = requests.get('http://'+request.get_host()+'/api/class/'+id+'/')
        form_fields = form_fields_req.json()
        form = AssignmentForm(initial={})
            
    return render(request, 'schoolapi/forms.html', {'form': form})