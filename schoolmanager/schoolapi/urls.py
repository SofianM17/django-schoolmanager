from django.urls import path, include
from . import views
from rest_framework import routers, viewsets

router = routers.DefaultRouter()
router.register('students', views.StudentView)
router.register('instructors', views.InstructorView)
router.register('class', views.ClassView)
router.register('clubs', views.ClubView)
router.register('events', views.EventView)
router.register('exams', views.ExamView)
router.register('homework', views.HomeworkView)
router.register('assignment', views.AssignmentView)
router.register('assignment', views.ExamPrepView)

urlpatterns = [
    path('', include(router.urls))
]