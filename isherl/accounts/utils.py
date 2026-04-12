from django.utils.crypto import get_random_string
from django.urls import reverse

from students.models import Student

def generate_student_id():
    """
    Generates a unique student ID like: STU-8F3K2A
    """
    return f"STU-{get_random_string(6).upper()}"


def generate_applicant_id():
    """
    Generates a unique applicant ID like: APP-4J9QX2
    """
    return f"APP-{get_random_string(6).upper()}"


def post_login_redirect(user):
    """
    Determines where to send the user after login
    based on their role (student/applicant).
    """
    if user.is_student:
        return reverse("students:dashboard")
    elif user.is_applicant:
        return reverse("applicant_dashboard")
    return reverse("home")



def convert_applicant_to_student(user):
    """
    Converts an applicant into a student safely.
    """
    user.is_applicant = False
    user.is_student = True

    if not user.student_id:
        user.student_id = generate_student_id()

    user.save()

    Student.objects.get_or_create(
        user=user,
        defaults={"student_id": user.student_id}
    )
