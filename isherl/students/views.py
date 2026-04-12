from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.decorators import student_required
from applications.models import Profile


@login_required
@student_required
def student_dashboard(request):
    """
    Main student dashboard.
    User is guaranteed to be a student by decorator.
    """
    profile = request.user.profile  # created via signal

    context = {
        "profile": profile,
        "student_id": request.user.student_id,
    }
    return render(request, "students/dashboard.html", context)


@login_required
@student_required
def student_profile(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    return render(request, "students/profile.html", {"profile": profile})


@login_required
@student_required
def student_courses(request):
    return render(request, "students/courses.html")


@login_required
@student_required
def student_payments(request):
    return render(request, "students/payments.html")


@login_required
@student_required
def student_documents(request):
    return render(request, "students/documents.html")
