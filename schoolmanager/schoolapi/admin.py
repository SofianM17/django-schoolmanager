from django.contrib import admin
from .models import User, Student, Instructor, Event, Club

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Event)
admin.site.register(Club)