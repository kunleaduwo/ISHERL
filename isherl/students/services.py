from students.models import Student
from .models import Student


def accept_application(application):
    user = application.applicant
    user.is_student = True
    user.is_applicant = False
    user.save()

    student = Student.objects.create(
        user=user,
        student_id=f"STU{user.id:05d}",
        application=application,
        course_name=application.course_name
    )
    return student
