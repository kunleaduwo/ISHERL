
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import login, logout as auth_logout, get_user_model
from django.core.mail import send_mail
from accounts.models import EmailVerification
from students.models import Student
from .forms import CustomUserCreationForm, CustomAuthenticationForm
import uuid
from django.contrib import messages
from django.http import Http404
from .utils import generate_student_id, generate_applicant_id
from django.contrib.auth.models import auth





# ------------------------------
# Registration / Email Verification
# ------------------------------

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.is_applicant = True
            user.is_student = False

            if not user.applicant_id:
                user.applicant_id = generate_applicant_id()
            user.save()

            # Email verification
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(str(user.pk).encode())
            verification_link = f"{request.scheme}://{request.get_host()}/accounts/verify-email/{uid}/{token}/"
            send_mail(
                'Email Verification',
                f'Click the link below to verify your email:\n\n{verification_link}',
                'no-reply@isherl.org',
                [user.email],
            )
            return redirect('accounts:verification_sent')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def verify_email(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_user_model().objects.get(pk=uid)
    except Exception:
        messages.error(request, "Invalid verification link")
        return redirect('accounts:login')

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Email verified! You can now log in.")
    else:
        messages.error(request, "Link invalid or expired.")
    return redirect('accounts:login')


def verification_sent(request):
    return render(request, 'accounts/verification_sent.html')


# ------------------------------
# Login / Logout
# ------------------------------

def custom_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Remember Me
            if form.cleaned_data.get('remember_me'):
                request.session.set_expiry(60 * 60 * 24 * 30)
            else:
                request.session.set_expiry(0)

            # Redirect to correct dashboard
            return redirect('accounts:dashboard_redirect')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('accounts:login')


# ------------------------------
# Dashboard Redirect
# ------------------------------
# @login_required
# def dashboard_redirect(request):
#     user = request.user

#     if user.is_student:
#         return redirect("students:student_dashboard")
#     elif user.is_applicant:
#         return redirect("applications:dashboard")
#     else:
#         return redirect("accounts:login")

@login_required
def dashboard_redirect(request):
    user = request.user

    if user.is_student:
        # Ensure Student record exists
        Student.objects.get_or_create(user=user, defaults={'student_id': generate_student_id()})
        return redirect('students:student_dashboard')
    elif user.is_applicant:
        return redirect('applications:dashboard')
    else:
        return redirect('accounts:login')


# ------------------------------
# Approve Applicant → Student
# ------------------------------

def approve_applicant(user):
    """
    Converts applicant to student and creates a Student record.
    """
    if not user.is_student:
        user.is_applicant = False
        user.is_student = True
        user.save()

        # Create Student record
        Student.objects.get_or_create(user=user, defaults={'student_id': generate_student_id()})


























# def verify_email(request, uidb64, token):
#     """
#     This handles email verification link clicks.
#     Activates user if token is valid.
#     """
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         user = get_user_model().objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
#         raise Http404("Invalid verification link")

#     if default_token_generator.check_token(user, token):
#         user.is_active = True
#         user.save()
#         messages.success(request, "Email verified successfully! You can now log in.")
#         return redirect('accounts:login')
#     else:
#         messages.error(request, "The verification link is invalid or expired.")
#         return redirect('accounts:login')




# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False               
#             user.is_applicant = True
#             user.is_student = False

#             # Generate applicant ID ONLY if not set
#             if not user.applicant_id:
#                 user.applicant_id = generate_applicant_id()
#             user.save()

#             # Email verification
#             token = default_token_generator.make_token(user)
#             uid = urlsafe_base64_encode(str(user.pk).encode())

#             verification_link = (
#                 f"{get_current_site(request).domain}"
#                 f"/accounts/verify-email/{uid}/{token}/"
#             )
#             send_mail(
#                 'Email Verification',
#                 f'Click the link below to verify your email:\n\n{verification_link}',
#                 'no-reply@isherl.org',
#                 [user.email],
#             )
#             return redirect('accounts:verification_sent')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'accounts/register.html', {'form': form})




# def verification_sent(request):
#     return render(request, 'accounts/verification_sent.html')




# @login_required
# def dashboard_redirect(request):
#     user = request.user

#     if user.is_student:
#         # Make sure Student record exists
#         from students.models import Student
#         Student.objects.get_or_create(
#             user=user,
#             defaults={'student_id': generate_student_id()}
#         )
#         return redirect('students:dashboard')
#     elif user.is_applicant:
#         return redirect('applications:dashboard')
#     else:
#         return redirect('accounts:login')




# def custom_login(request):
#     if request.method == 'POST':
#         form = CustomAuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)

#             # Remember Me
#             if form.cleaned_data.get('remember_me'):
#                 request.session.set_expiry(60 * 60 * 24 * 30)
#             else:
#                 request.session.set_expiry(0)

#             # Redirect to proper dashboard
#             return redirect('accounts:dashboard_redirect')
#     else:
#         form = CustomAuthenticationForm()

#     return render(request, 'accounts/login.html', {'form': form})




# def approve_applicant(user):
#     """
#     Convert an applicant into a student with a new student ID.
#     """
#     if not user.is_student:
#         user.is_applicant = False
#         user.is_student = True
#         user.save()

#         # Create a Student record if it doesn't exist
#         Student.objects.get_or_create(
#             user=user,
#             defaults={'student_id': generate_student_id()}
#         )



# def logout(request):
#     auth.logout(request)
    
#     return redirect("accounts:login ")











