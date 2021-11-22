from django.urls import path, include
from . import views
from rest_framework import routers, viewsets

router = routers.DefaultRouter()
router.register('students', views.StudentView)
router.register('instructors', views.InstructorView)
router.register('class', views.ClassView)
router.register('clubs', views.ClubView)
router.register('events', views.EventView)
router.register('exam', views.ExamView)
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

    path('add-club/', views.addClub),
    path('delete-club/<id>', views.deleteClub, name='delete-club'),
    path('update-club/<id>', views.updateClub, name='update-club'),

    path('add-event/', views.addEvent),
    path('delete-event/<id>', views.deleteEvent, name='delete-event'),
    path('update-event/<id>', views.updateEvent, name='update-event'),

    path('add-exam/', views.addExam),
    path('delete-exam/<id>', views.deleteExam, name='delete-exam'),
    path('update-exam/<id>', views.updateExam, name='update-exam'),
    
    path('add-homework/', views.addHomework),
    path('delete-homework/<id>', views.deleteHomework, name='delete-homework'),
    path('update-homework/<id>', views.updateHomework, name='update-homework'),

    path('add-assignment/', views.addAssignment),
    path('delete-assignment/<id>', views.deleteAssignment, name='delete-assignment'),
    path('update-assignment/<id>', views.updateAssignment, name='update-assignment'),
]