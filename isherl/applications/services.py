
from students.models import Student
from django.utils.crypto import get_random_string

def accept_application(application):
    user = application.applicant
    
    if user.is_student:
        return

    # Update user role
    user.is_student = True
    user.is_applicant = False
    user.save()

    Student.objects.create(
        user=user,
        student_id=f"STD-{get_random_string(8).upper()}"
    )


    # Update application status
    application.status = 'accepted'
    application.save()
    
    return
