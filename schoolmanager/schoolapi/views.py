from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
import requests
from .forms import *
from django.http import HttpResponseRedirect
from django.db.models import Sum
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

# API
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class StudentView(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class InstructorView(viewsets.ModelViewSet):
#     queryset = Instructor.objects.all()
#     serializer_class = InstructorSerializer
    
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
    # response = requests.get('http://'+request.get_host()+'/api/class/')
    # classes = response.json()

    # response = requests.get('http://'+request.get_host()+'/api/exam/')
    # exams = response.json()

    # response = requests.get('http://'+request.get_host()+'/api/homework/')
    # homework = response.json()

    # response = requests.get('http://'+request.get_host()+'/api/assignment/')
    # assignments = response.json()

    # response = requests.get('http://'+request.get_host()+'/api/clubs/')
    # clubs = response.json()

    # response = requests.get('http://'+request.get_host()+'/api/events/')
    # events = response.json()

    # response = requests.get('http://'+request.get_host()+'/api/exam_prep/')
    # exam_prep = response.json()

    # response = requests.get('http://'+request.get_host()+'/api/finance/')
    # finance = response.json()
    if request.user.is_authenticated:
        classes = Class.objects.all()
        if request.user.is_student:
            return render(request, "schoolapi/dashboard.html", {'classes': classes})
        if request.user.is_instructor:
            return render(request, "schoolapi/dashboard_instructor.html", {'classes': classes})
        return render(request, "schoolapi/dashboard.html", {'classes': classes})
    return HttpResponseRedirect("/login")
    #{"classes" : classes, 
    #"exams" : exams, "homework" : homework, "assignments" : assignments, "clubs" : clubs,
    #"events" : events, "exam_prep" : exam_prep, "finance" : finance}

def finances(request):
    if request.user.is_authenticated:
        finance = Finance.objects.all()
        return render(request, "schoolapi/finances.html", {'finance': finance})
    return HttpResponseRedirect("/login")

def tasks(request):
    if request.user.is_authenticated:
        if request.user.is_student:
            exams = Exam.objects.all()
            exam_prep = ExamPrep.objects.all()
            homework = Homework.objects.all()
            assignments = Assignment.objects.all()
            return render(request, "schoolapi/tasks.html", {'exams': exams, 'exam_prep': exam_prep,
            'homework': homework, 'assignments': assignments})
        if request.user.is_instructor:
            exams = Exam.objects.all()
            exam_prep = ExamPrep.objects.all()
            homework = Homework.objects.all()
            assignments = Assignment.objects.all()
            return render(request, "schoolapi/tasks_instructor.html", {'exams': exams, 'exam_prep': exam_prep,
            'homework': homework, 'assignments': assignments})
    return HttpResponseRedirect("/login")

def clubsEvents(request):
    if request.user.is_authenticated:
        clubs = Club.objects.all()
        events = Event.objects.all()
        return render(request, "schoolapi/clubsEvents.html", {'clubs': clubs, 'events': events})
    return HttpResponseRedirect("/login")

##### Class CRUD #####
def addClass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ClassForm(request.POST)
            if form.is_valid():
                request.user.class_set.create(
                    name=form.cleaned_data["name"],
                    time=form.cleaned_data["time"],
                    section=form.cleaned_data["section"],
                    room=form.cleaned_data["room"]

                    )
                #form.save()
                return HttpResponseRedirect("/")
                
        else:
            form = ClassForm()
        return render(request, 'schoolapi/forms.html', {'form': form})
    return HttpResponseRedirect("/login")

def deleteClass(request, id):
    if request.user.is_authenticated:
        class_data = Class.objects.get(id=id)
        if request.method == 'POST':
            class_data.delete()
            return HttpResponseRedirect("/")
        return render(request, "schoolapi/delete_view.html", {"data": class_data})
    return HttpResponseRedirect("/login")

def updateClass(request, id):
    if request.user.is_authenticated:
        class_data = Class.objects.get(id=id)
        form = ClassForm(instance=class_data)
        if request.method == 'POST':
            form = ClassForm(request.POST, instance=class_data)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect("/")
                
        return render(request, 'schoolapi/forms.html', {'form': form})
    return HttpResponseRedirect("/login")

##### Club CRUD #####
def addClub(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ClubForm(request.POST)
            if form.is_valid():
                request.user.club_set.create(
                    name=form.cleaned_data["name"],
                    meeting_time=form.cleaned_data["meeting_time"],
                )
                return HttpResponseRedirect("/clubsEvents")
        else:
            form = ClubForm()
                
        return render(request, 'schoolapi/forms.html', {'form': form})
    return HttpResponseRedirect("/login")

def deleteClub(request, id):
    if request.user.is_authenticated:
        club_data = Club.objects.get(id=id)
        if request.method == 'POST':
            club_data.delete()
            return HttpResponseRedirect("/clubsEvents")
        return render(request, "schoolapi/delete_view.html", {"data": club_data})
    return HttpResponseRedirect("/login")

def updateClub(request, id):
    if request.user.is_authenticated:
        club_data = Club.objects.get(id=id)
        form = ClubForm(instance=club_data)
        if request.method == 'POST':
            form = ClubForm(request.POST, instance=club_data)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/clubsEvents")
                
        return render(request, 'schoolapi/forms.html', {'form': form})
    return HttpResponseRedirect("/login")

##### Event CRUD #####
def addEvent(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EventForm(request.POST, user=request.user)
            if form.is_valid():
                request.user.event_set.create(
                    name=form.cleaned_data["name"],
                    date=form.cleaned_data["date"],
                    description=form.cleaned_data["description"],
                    host=form.cleaned_data["host"],
                    type=form.cleaned_data["type"],
                    club=form.cleaned_data["club"],
                )
                return HttpResponseRedirect("/clubsEvents")
                
        else:
            form = EventForm(user=request.user)
                
        return render(request, 'schoolapi/forms.html', {'form': form})
    return HttpResponseRedirect("/login")

def deleteEvent(request, id):
    if request.user.is_authenticated:
        event_data = Event.objects.get(id=id)
        if request.method == 'POST':
            event_data.delete()
            return HttpResponseRedirect("/clubsEvents")
        return render(request, "schoolapi/delete_view.html", {"data": event_data})
    return HttpResponseRedirect("/login")

def updateEvent(request, id):
    if request.user.is_authenticated:
        event_data = Event.objects.get(id=id)
        form = EventForm(instance=event_data, user=request.user)
        if request.method == 'POST':
            form = EventForm(request.POST, instance = event_data, user=request.user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/clubsEvents")
                
        return render(request, 'schoolapi/forms.html', {'form': form})
    return HttpResponseRedirect("/login")
    
##### Exam CRUD #####
def addExam(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ExamForm(request.POST, user=request.user)
            if form.is_valid():
                request.user.exam_set.create(
                className=form.cleaned_data["className"],
                task_name=form.cleaned_data["task_name"],
                date=form.cleaned_data["date"],
                description=form.cleaned_data["description"],
                priority=form.cleaned_data["priority"],
                start_time=form.cleaned_data["start_time"],
                room=form.cleaned_data["room"]
                )
                return HttpResponseRedirect("/tasks")
                
        else:
            form = ExamForm(user=request.user)
                
        return render(request, 'schoolapi/forms.html', {'form': form})
    return HttpResponseRedirect("/login")

def deleteExam(request, id):
    if request.user.is_authenticated:
        exam_data = Exam.objects.get(id=id)
        if request.method == 'POST':
            exam_data.delete()
            return HttpResponseRedirect("/tasks")
        return render(request, "schoolapi/delete_view.html", {"data": exam_data})
    return HttpResponseRedirect("/login")

def updateExam(request, id):
    if request.user.is_authenticated:
        exam_data = Exam.objects.get(id=id)
        form = ExamForm(instance=exam_data, user=request.user)
        if request.method == 'POST':
            form = ExamForm(request.POST, instance=exam_data, user=request.user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/tasks")
                
        return render(request, 'schoolapi/forms.html', {'form': form})
    return HttpResponseRedirect("/login")

 ##### Homework CRUD #####
def addHomework(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = HomeworkForm(request.POST, user=request.user)
            if form.is_valid():
                request.user.homework_set.create(
                className=form.cleaned_data["className"],
                task_name=form.cleaned_data["task_name"],
                date=form.cleaned_data["date"],
                description=form.cleaned_data["description"],
                priority=form.cleaned_data["priority"],
                no_questions=form.cleaned_data["no_questions"],

                )
                #form.save()
                return HttpResponseRedirect("/tasks")
                
        else:
            form = HomeworkForm(user=request.user)
                
        return render(request, 'schoolapi/forms.html', {'form': form})
    return HttpResponseRedirect("/login")

def deleteHomework(request, id):
    if request.user.is_authenticated:
        homework_data = Homework.objects.get(id=id)
        if request.method == 'POST':
            homework_data.delete()
            return HttpResponseRedirect("/tasks")
        return render(request, "schoolapi/delete_view.html", {})
    return HttpResponseRedirect("/login")

def updateHomework(request, id):
    if request.user.is_authenticated:
        homework_data = Homework.objects.get(id=id)
        form = HomeworkForm(instance=homework_data, user=request.user)
        if request.method == 'POST':
            form = HomeworkForm(request.POST, instance=homework_data, user=request.user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/tasks")

        return render(request, 'schoolapi/forms.html', {'form': form})
    return HttpResponseRedirect("/login")

##### Assignment CRUD #####
def addAssignment(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AssignmentForm(request.POST, user=request.user)
            if form.is_valid():
                request.user.assignment_set.create(
                    className=form.cleaned_data["className"],
                    task_name=form.cleaned_data["task_name"],
                    date=form.cleaned_data["date"],
                    description=form.cleaned_data["description"],
                    priority=form.cleaned_data["priority"],
                    group_members=form.cleaned_data["group_members"],
                    module=form.cleaned_data["module"],
                )
                #form.save()
                return HttpResponseRedirect("/tasks")
        else:
            form = AssignmentForm(user=request.user)
                
        return render(request, 'schoolapi/forms.html', {'form': form})
    return HttpResponseRedirect("/login")

def deleteAssignment(request, id):
    if request.user.is_authenticated:
        assignment_data = Assignment.objects.get(id=id)
        if request.method == 'POST':
            assignment_data.delete()
            #requests.delete('http://'+request.get_host()+'/api/assignment/'+id+'/')
            return HttpResponseRedirect("/tasks")
        return render(request, "schoolapi/delete_view.html", {})
    return HttpResponseRedirect("/login")

def updateAssignment(request, id):
    if request.user.is_authenticated:
        assignment_data = Assignment.objects.get(id=id)
        form = AssignmentForm(instance=assignment_data, user=request.user)
        if request.method == 'POST':
            form = AssignmentForm(request.POST, instance=assignment_data, user=request.user)
            if form.is_valid():
                form.save()
            # form = form.cleaned_data
                #requests.put('http://'+request.get_host()+'/api/assignment/'+id+'/', form)
                return HttpResponseRedirect("/tasks")
        # else:
        #     form_fields_req = requests.get('http://'+request.get_host()+'/api/assignment/'+id+'/')
        #     form_fields = form_fields_req.json()
        #     form = AssignmentForm(initial={"username": form_fields['username'], "name": form_fields['name'],
        #     "date": form_fields['date'], "description": form_fields['description'],
        #     "priority": form_fields['priority'], "group_members": form_fields['group_members'],
        #     "module": form_fields['module']})
                
        return render(request, 'schoolapi/forms.html', {'form': form})
    return HttpResponseRedirect("/login")

 ##### exam_prep CRUD #####
def addExamPrep(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ExamPrepForm(request.POST, user=request.user)
            if form.is_valid():
                form.instance.user = request.user
                request.user.examprep_set.create(
                    exam=form.cleaned_data["exam"],
                    prep_type=form.cleaned_data["prep_type"],
                )
                return HttpResponseRedirect("/tasks")
                
        else:
            form = ExamPrepForm(user=request.user)
                
        return render(request, 'schoolapi/forms.html', {'form': form})
    return HttpResponseRedirect("/login")

def deleteExamPrep(request, id):
    if request.user.is_authenticated:
        examPrep_data = ExamPrep.objects.get(id=id)
        if request.method == 'POST':
            examPrep_data.delete()
            return HttpResponseRedirect("/tasks")
        return render(request, "schoolapi/delete_view.html", {})
    return HttpResponseRedirect("/login")

def updateExamPrep(request, id):
    if request.user.is_authenticated:
        examPrep_data = ExamPrep.objects.get(id=id)
        form = ExamPrepForm(instance=examPrep_data)
        if request.method == 'POST':
            form = ExamPrepForm(request.POST, instance=examPrep_data)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/tasks")

        return render(request, 'schoolapi/forms.html', {'form': form})
    return HttpResponseRedirect("/login")

 ##### Finance CRUD #####
def addFinance(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = FinanceForm(request.POST)
            if form.is_valid():
                request.user.finance_set.create(
                    initialBudget=form.cleaned_data["initialBudget"],
                    income=form.cleaned_data["income"],
                    tuition=form.cleaned_data["tuition"],
                    equipment=form.cleaned_data["equipment"],
                    books=form.cleaned_data["books"],

                )
                return HttpResponseRedirect("/finances")
                
        else:
            form = FinanceForm()
                
        return render(request, 'schoolapi/forms.html', {'form': form})
    return HttpResponseRedirect("/login")
    
def deleteFinance(request, id):
    if request.user.is_authenticated:
        finance_data = Finance.objects.get(id=id)
        if request.method == 'POST':
            finance_data.delete()
            return HttpResponseRedirect("/finances")
        return render(request, "schoolapi/delete_view.html", {})
    return HttpResponseRedirect("/login")

def updateFinancePos(request, id):
    if request.user.is_authenticated:
        finance_data = Finance.objects.get(id=id)
        form = FinancePosForm(instance=finance_data)
        if request.method == 'POST':
            form = FinancePosForm(request.POST, instance=finance_data)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/finances")

        return render(request, 'schoolapi/forms.html', {'form': form})
    return HttpResponseRedirect("/login")

def updateFinanceNeg(request, id):
    if request.user.is_authenticated:
        finance_data = Finance.objects.get(id=id)
        form = FinanceNegForm(instance=finance_data)
        if request.method == 'POST':
            form = FinanceNegForm(request.POST, instance=finance_data)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/finances")

        return render(request, 'schoolapi/forms.html', {'form': form})
    return HttpResponseRedirect("/login")