from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages


def applicant_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(settings.LOGIN_URL)

        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)

        if not getattr(request.user, "is_applicant", False):
            return redirect("dashboard")

        return view_func(request, *args, **kwargs)

    return _wrapped_view


def student_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_student:
            messages.error(request, "Student access only.")
            return redirect(settings.LOGIN_URL)
        return view_func(request, *args, **kwargs)
    return wrapper
