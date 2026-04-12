from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'accounts'


urlpatterns = [
    # Registration & Email Verification
    path('register/', views.register, name='register'),
    path('verify-email/<uidb64>/<token>/', views.verify_email, name='email_verification'),
    path('verification-sent/', views.verification_sent, name='verification_sent'),
    path('dashboard/', views.dashboard_redirect, name='dashboard_redirect'),
        

    # Login & Logout
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("login/", views.custom_login, name="login"),
    path("logout/", views.logout_view, name="logout"),

    # # Password Reset
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    
    # Other URLs...
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


] 
# urlpatterns += tf_urls

    



