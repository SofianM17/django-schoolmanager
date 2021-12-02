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

    response = requests.get('http://'+request.get_host()+'/api/exam/')
    exams = response.json()

    response = requests.get('http://'+request.get_host()+'/api/homework/')
    homework = response.json()

    response = requests.get('http://'+request.get_host()+'/api/assignment/')
    assignments = response.json()

    response = requests.get('http://'+request.get_host()+'/api/clubs/')
    clubs = response.json()

    response = requests.get('http://'+request.get_host()+'/api/events/')
    events = response.json()

    response = requests.get('http://'+request.get_host()+'/api/exam_prep/')
    exam_prep = response.json()

    response = requests.get('http://'+request.get_host()+'/api/finance/')
    finance = response.json()

    return render(request, "schoolapi/dashboard.html", {"classes" : classes, 
    "exams" : exams, "homework" : homework, "assignments" : assignments, "clubs" : clubs,
    "events" : events, "exam_prep" : exam_prep, "finance" : finance})

##### Class CRUD #####
def addClass(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
            
    else:
        form = ClassForm()
            
    return render(request, 'schoolapi/forms.html', {'form': form})

def deleteClass(request, id):
    class_data = Class.objects.get(id=id)
    if request.method == 'POST':
        class_data.delete()
        return HttpResponseRedirect("/")
    return render(request, "schoolapi/delete_view.html", {"data": class_data})

def updateClass(request, id):
    class_data = Class.objects.get(id=id)
    form = ClassForm(instance=class_data)
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=class_data)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/")
            
    return render(request, 'schoolapi/forms.html', {'form': form})

##### Club CRUD #####
def addClub(request):
    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
            
    else:
        form = ClubForm()
            
    return render(request, 'schoolapi/forms.html', {'form': form})

def deleteClub(request, id):
    club_data = Club.objects.get(id=id)
    if request.method == 'POST':
        club_data.delete()
        return HttpResponseRedirect("/")
    return render(request, "schoolapi/delete_view.html", {"data": club_data})

def updateClub(request, id):
    club_data = Club.objects.get(id=id)
    form = ClubForm(instance=club_data)
    if request.method == 'POST':
        form = ClubForm(request.POST, instance=club_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
            
    return render(request, 'schoolapi/forms.html', {'form': form})

##### Event CRUD #####
def addEvent(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
            
    else:
        form = EventForm()
            
    return render(request, 'schoolapi/forms.html', {'form': form})

def deleteEvent(request, id):
    event_data = Event.objects.get(id=id)
    if request.method == 'POST':
        event_data.delete()
        return HttpResponseRedirect("/")
    return render(request, "schoolapi/delete_view.html", {"data": event_data})

def updateEvent(request, id):
    event_data = Event.objects.get(id=id)
    form = EventForm(instance=event_data)
    if request.method == 'POST':
        form = EventForm(request.POST, instance = event_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
            
    return render(request, 'schoolapi/forms.html', {'form': form})

##### Exam CRUD #####
def addExam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
            
    else:
        form = ExamForm()
            
    return render(request, 'schoolapi/forms.html', {'form': form})

def deleteExam(request, id):
    exam_data = Exam.objects.get(id=id)
    if request.method == 'POST':
        exam_data.delete()
        return HttpResponseRedirect("/")
    return render(request, "schoolapi/delete_view.html", {})

def updateExam(request, id):
    exam_data = Exam.objects.get(id=id)
    form = ExamForm(instance=exam_data)
    if request.method == 'POST':
        form = ExamForm(request.POST, instance=exam_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
            
    return render(request, 'schoolapi/forms.html', {'form': form})

 ##### Homework CRUD #####
def addHomework(request):
    if request.method == 'POST':
        form = HomeworkForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
            
    else:
        form = HomeworkForm()
            
    return render(request, 'schoolapi/forms.html', {'form': form})

def deleteHomework(request, id):
    homework_data = Homework.objects.get(id=id)
    if request.method == 'POST':
        homework_data.delete()
        return HttpResponseRedirect("/")
    return render(request, "schoolapi/delete_view.html", {})

def updateHomework(request, id):
    homework_data = Homework.objects.get(id=id)
    form = HomeworkForm(instance=homework_data)
    if request.method == 'POST':
        form = HomeworkForm(request.POST, instance=homework_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

    return render(request, 'schoolapi/forms.html', {'form': form})

##### Assignment CRUD #####
def addAssignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            #form = form.cleaned_data
            #requests.post('http://'+request.get_host()+'/api/assignment/', form)
        return HttpResponseRedirect("/")
            
    else:
        form = AssignmentForm()
            
    return render(request, 'schoolapi/forms.html', {'form': form})

def deleteAssignment(request, id):
    assignment_data = Assignment.objects.get(id=id)
    if request.method == 'POST':
        assignment_data.delete()
        #requests.delete('http://'+request.get_host()+'/api/assignment/'+id+'/')
        return HttpResponseRedirect("/")
    return render(request, "schoolapi/delete_view.html", {})

def updateAssignment(request, id):
    assignment_data = Assignment.objects.get(id=id)
    form = AssignmentForm(instance=assignment_data)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment_data)
        if form.is_valid():
            form.save()
           # form = form.cleaned_data
            #requests.put('http://'+request.get_host()+'/api/assignment/'+id+'/', form)
            return HttpResponseRedirect("/")
    # else:
    #     form_fields_req = requests.get('http://'+request.get_host()+'/api/assignment/'+id+'/')
    #     form_fields = form_fields_req.json()
    #     form = AssignmentForm(initial={"username": form_fields['username'], "name": form_fields['name'],
    #     "date": form_fields['date'], "description": form_fields['description'],
    #     "priority": form_fields['priority'], "group_members": form_fields['group_members'],
    #     "module": form_fields['module']})
            
    return render(request, 'schoolapi/forms.html', {'form': form})

 ##### exam_prep CRUD #####
def addExamPrep(request):
    if request.method == 'POST':
        form = ExamPrepForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
            
    else:
        form = ExamPrepForm()
            
    return render(request, 'schoolapi/forms.html', {'form': form})

def deleteExamPrep(request, id):
    examPrep_data = ExamPrep.objects.get(id=id)
    if request.method == 'POST':
        examPrep_data.delete()
        return HttpResponseRedirect("/")
    return render(request, "schoolapi/delete_view.html", {})

def updateExamPrep(request, id):
    examPrep_data = Homework.objects.get(id=id)
    form = ExamPrepForm(instance=examPrep_data)
    if request.method == 'POST':
        form = HomeworkForm(request.POST, instance=examPrep_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

    return render(request, 'schoolapi/forms.html', {'form': form})

 ##### Finance CRUD #####
def addFinance(request):
    if request.method == 'POST':
        form = FinanceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
            
    else:
        form = FinanceForm()
            
    return render(request, 'schoolapi/forms.html', {'form': form})

def deleteFinance(request, id):
    finance_data = Finance.objects.get(id=id)
    if request.method == 'POST':
        finance_data.delete()
        return HttpResponseRedirect("/")
    return render(request, "schoolapi/delete_view.html", {})

def updateFinance(request, id):
    finance_data = Finance.objects.get(id=id)
    form = FinanceForm(instance=finance_data)
    if request.method == 'POST':
        form = FinanceForm(request.POST, instance=finance_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

    return render(request, 'schoolapi/forms.html', {'form': form})