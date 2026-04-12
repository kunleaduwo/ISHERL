from django.conf import settings
from django.shortcuts import redirect


class RoleBasedRedirectMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        path = request.path

        if not user.is_authenticated:
            return self.get_response(request)

        # Allow login, logout, admin, static/media
        if (
            path.startswith("/admin/")
            or path.startswith("/static/")
            or path.startswith("/media/")
            or settings.LOGIN_URL in path
        ):
            return self.get_response(request)

        # Role-based redirects
        if user.is_student and not path.startswith("/students/"):
            return redirect("student_dashboard")

        if user.is_applicant and not path.startswith("/applicants/"):
            return redirect("applicant_dashboard")

        return self.get_response(request)
