from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path('apply/', views.application_form, name='application_form'),
    path('redirect-after-login/', views.redirect_after_login, name='redirect_after_login'),
    
    # path("application/<int:pk>/view/", views.application_update, name="application_view"),
    
    path('status/', views.application_status_view, name='application_status'),

    path("profile-photo/",views.profile_photo,name="profile_photo"),
    
    # path("dashboard/", views.user_dashboard, name="user_dashboard"),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    path('entry-requirements/', views.entry_requirements, name='entry-requirements'),
    path('find-a-course/', views.find_a_course, name='find_a_course'),
    path('how-to-apply/', views.how_to_apply, name='how_to_apply'),
    path('application/', views.application_form, name='apply'),
    
    path('personal-info/', views.personal_info, name='personal-info'),
    path('documents/', views.documents, name='documents'),
    
    path('payment-success/', views.payment_success, name='payment-success'),
    
    path("payment/initiate/<int:application_id>/", views.initiate_payment, name="initiate-payment"),
    path("payment/verify/", views.verify_payment, name="verify-payment"),
]



