from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.contrib.auth import login

import uuid
import requests

from .models import Application, Payment, Profile, User
from .forms import ApplicationForm, PersonalInfoForm
from .services import accept_application
from accounts.decorators import applicant_required
from students.utils import create_student_from_application

# -------------------------
# Profile Management
# -------------------------
@login_required
def profile_photo(request):
    profile = request.user.profile

    if request.method == "POST":
        photo = request.FILES.get("photo")
        if photo:
            profile.photo = photo
            profile.save()
            messages.success(request, "Profile photo updated successfully")
            return redirect("applications:application_form")

    return render(request, "applications/profile_photo.html", {"profile": profile})


# -------------------------
# Redirect after login
# -------------------------
@login_required
def redirect_after_login(request):
    user = request.user

    # Automatically promote accepted applicants to students
    if user.is_applicant:
        try:
            application = user.applications_as_applicant
        except Application.DoesNotExist:
            application = None

        if application and application.status == "accepted":
            # Promote user
            create_student_from_application(application)

            # Refresh session so the current request sees the updated role
            user = type(user).objects.get(pk=user.pk)  # reload from DB
            login(request, user)  # updates session

    # Redirect based on the user's role
    if user.is_student:
        return redirect("student_dashboard")
    elif user.is_applicant:
        return redirect("applicant_dashboard")
    else:
        return redirect("")  # fallback page



# -------------------------
# Generic dashboard
# -------------------------
@login_required(login_url='two_factor:login') 
def dashboard(request):
    return render(request, 'applications/dashboard.html', {'applicant_id': request.user.id})


# -------------------------
# Personal info
# -------------------------
@login_required
def personal_info(request):
    application = get_object_or_404(Application, applicant=request.user)
    
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST, instance=application)
        if form.is_valid():
            form.save(commit=False)
            application.personal_info_completed = True
            application.save()
            return redirect('applicant_dashboard')
    else:
        form = PersonalInfoForm(instance=application)
    
    return render(request, 'dashboard/applications/personal_info.html', {
        'form': form,
        'application': application,
    })


# -------------------------
# Admin: accept application
# -------------------------
@login_required
@staff_member_required
def accept_application_view(request, pk):
    application = get_object_or_404(Application, pk=pk)

    # If application is already accepted, don't process again
    if application.status == 'accepted':
        return redirect('admin_dashboard')  # Or some appropriate fallback

    # Accept the application and promote to student
    accept_application(application)
    
     # Reload the user to update session info
    user = application.applicant
    user = User.objects.get(pk=user.pk)  # Refresh from DB
    login(request, user)  # Update session with new is_student


    # Now the user is a student, so redirect them to the student dashboard
    return redirect('student_dashboard')



# -------------------------
# Application form (create/edit)
# -------------------------
@login_required
@applicant_required
def application_form(request):
    """
    Create or edit an application. Blocks editing if already paid.
    """
    application, created = Application.objects.get_or_create(applicant=request.user)

    if application.is_paid:
        messages.info(request, "You cannot edit the application after payment.")
        return redirect("aaplications:applicant_dashboard")

    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES, instance=application)
        if form.is_valid():
            app = form.save(commit=False)
            app.applicant = request.user

            if not app.application_id:
                app.application_id = f"APP-{uuid.uuid4().hex[:8].upper()}"

            app.save()
            messages.success(request, "Application saved successfully!")

            # Redirect to payment
            return redirect("initiate_payment", application_id=app.id)
    else:
        form = ApplicationForm(instance=application)

    return render(request, "applications/application_form.html", {
        "form": form,
        "application": application
    })


# -------------------------
# Applicant dashboard
# -------------------------
@login_required
@applicant_required  
def applicant_dashboard(request):
    application = Application.objects.filter(applicant=request.user).first()
    return render(request, "dashboard/application_dasboard.html", {"application": application})


# -------------------------
# Payment handling
# -------------------------
@login_required
@applicant_required
def initiate_payment(request, application_id):
    application = get_object_or_404(Application, id=application_id)

    if application.is_paid:
        return redirect("application_status")

    reference = str(uuid.uuid4())

    payment = Payment.objects.create(
        application=application,
        reference=reference,
        amount=15000,
        payment_type='application_fee'
    )

    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "email": application.email,
        "amount": payment.amount * 100,
        "reference": reference,
        "callback_url": request.build_absolute_uri("/payment/verify/")
    }

    response = requests.post(
        "https://api.paystack.co/transaction/initialize",
        json=data,
        headers=headers
    )

    res = response.json()
    if not res.get("status"):
        return render(request, "applications/payment_error.html", {"error": res})

    return redirect(res["data"]["authorization_url"])


@login_required
def verify_payment(request):
    reference = request.GET.get("reference")
    payment = get_object_or_404(Payment, reference=reference)

    headers = {"Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"}
    response = requests.get(f"https://api.paystack.co/transaction/verify/{reference}", headers=headers)
    data = response.json().get("data", {})

    if data.get("status") == "success":
        with transaction.atomic():
            payment.is_paid = True
            payment.save()

            application = payment.application
            application.is_paid = True
            application.save()

            send_mail(
                subject="Payment Successful – Application Received",
                message=f"Dear {application.full_name},\n\nThank you for paying your application fee.\nYour application is now under review.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[application.email],
            )

        return render(request, "applications/payment_success.html")

    return render(request, "applications/payment_failed.html")


def payment_success(request):
    return render(request, 'applications/payment_success.html')


# -------------------------
# Application status
# -------------------------

@login_required
@applicant_required
def application_status_view(request):
    application = Application.objects.filter(applicant=request.user).first()
    return render(request, 'applications/application_status.html', {'application': application})


# -------------------------
# Static info pages
# -------------------------
def entry_requirements(request):
    return render(request, 'applications/entry_requirements.html')


def find_a_course(request):
    return render(request, 'applications/find_a_course.html')


def how_to_apply(request):
    return render(request, 'applications/how_to_apply.html')


def documents(request):
    return render(request, 'applications/documents.html')
