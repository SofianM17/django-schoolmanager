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
router.register('exam_prep', views.ExamPrepView)
router.register('finance', views.FinanceView)

urlpatterns = [
    path('api/', include(router.urls), name='api'),
    path('', views.dashboard),

    path('add-class/', views.addClass),
    path('delete-class/<id>', views.deleteClass, name='delete-class'),
    path('update-class/<id>', views.updateClass, name='update-class'),

    path('add-exam/', views.addExam),
    
    path('add-homework/', views.addHomework),

    path('add-assignment/', views.addAssignment),
]