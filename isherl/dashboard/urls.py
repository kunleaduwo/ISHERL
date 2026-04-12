from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_router, name='dashboard'),
    path('applicant/', views.applicant_dashboard, name='applicant_dashboard'),
    path('student/', views.student_dashboard, name='student_dashboard'),
]
