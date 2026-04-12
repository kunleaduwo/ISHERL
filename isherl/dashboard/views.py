from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


# @login_required
# def dashboard_router(request):
#     if request.user.is_student:
#         return redirect('student_dashboard')
#     return redirect('applicant_dashboard')


@login_required
def dashboard_router(request):
    if request.user.is_student:
        return redirect('student_dashboard')
    elif request.user.is_applicant:
        return redirect('applicant_dashboard')
    return redirect('logout')

@login_required
def applicant_dashboard(request):
    # Show application details
    return render(request, 'dashboard/applicant_dashboard.html')

@login_required
def student_dashboard(request):
    # Show student details
    return render(request, 'dashboard/student_dashboard.html')






