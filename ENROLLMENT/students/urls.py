from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),       # /students/
    path('add/', views.add_student, name='add_student'),     # /students/add/
    path('edit/<int:pk>/', views.edit_student, name='edit_student'),  # /students/edit/1/
]

