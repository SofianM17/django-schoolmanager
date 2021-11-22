from rest_framework import serializers
from .models import *
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'username', 'school', 'program')

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ('id', 'username', 'school', 'faculty')

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('id', 'name', 'time', 'section', 'room')

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ('id', 'username', 'name', 'meeting_time')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'date', 'description', 'host', 'type', 'club', 'username')

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ('id', 'username', 'name', 'name_name', 'date', 'description', 'priority', 'time_limit', 'room')

class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ('id', 'username', 'name', 'name_name', 'date', 'description', 'priority', 'no_questions')

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ('id', 'username', 'name', 'name_name', 'date', 'description', 'priority', 'group_members', 'module')

class ExamPrepSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamPrep
        fields = ('id', 'exam', 'prep_type')

class FinanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finance
        fields = ('id', 'initialBudget', 'income', 'tuition', 'equipment', 'books', 'student')