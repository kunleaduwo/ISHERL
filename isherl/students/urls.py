from django.urls import path
from . import views


app_name = 'students'


urlpatterns = [
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path("profile/", views.student_profile, name="profile"),
    path("courses/", views.student_courses, name="courses"),
    path("payments/", views.student_payments, name="payments"),
    path("documents/", views.student_documents, name="documents"),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),

]






