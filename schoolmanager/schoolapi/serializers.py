from rest_framework import serializers
from .models import *
from register.models import *
from django.contrib.auth.models import User
from register.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'school', 'is_student', 'is_instructor']

# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ('id', 'user', 'school', 'program')

# class InstructorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Instructor
#         fields = ('id', 'user', 'school', 'faculty')

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('id', 'user', 'name', 'time', 'section', 'room')

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ('id', 'name', 'meeting_time')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'date', 'description', 'host', 'type', 'club', 'club_name')

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ('id', 'user', 'className', 'task_name', 'date', 'description', 'priority', 'start_time', 'room')

class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ('id', 'user', 'className', 'task_name', 'date', 'description', 'priority', 'no_questions')

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ('id', 'user', 'className', 'task_name', 'date', 'description', 'priority', 'group_members', 'module')

class ExamPrepSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamPrep
        fields = ('id', 'exam', 'prep_type')

class FinanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finance
        fields = ('id', 'initialBudget', 'income', 'tuition', 'equipment', 'books')