from rest_framework import serializers
from .models import User, Student, Instructor, Event, Club

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'school')