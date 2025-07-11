from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_student, name='add_student'),
    path('search/', views.search_student, name='search_student'),
    path('all/', views.view_all_students, name='view_all_students'),  
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),


]
