import random
from .models import Student



def generate_student_id(user):
    # Example: user.id = 1 -> STU-00001
    return f"STU-{user.id:05d}"

def create_student_from_application(application):
    # Ensure we have the applicant user
    user = application.applicant

    # Create student record
    Student.objects.create(
        user=user,
        application=application,
        student_id=generate_student_id(user)
    )

    # Update user roles
    user.is_applicant = False
    user.is_student = True
    user.save()
