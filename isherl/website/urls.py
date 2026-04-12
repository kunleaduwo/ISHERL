from django.urls import path
from . import views


app_name='website'


urlpatterns = [
    path('',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('courses/', views.course_list, name = "course_list"),
    path('courses/<int:pk>/course_detail/', views.course_detail, name='course_detail'),
    
    path('events/',views.event_list, name='events'),
    path('events/<int:pk>/event_detail/', views.event_detail, name='event_detail'),
    
    path('publications/', views.publications, name='publications'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name = 'contact'), 
    
]
