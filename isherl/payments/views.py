from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .services import mark_application_as_paid
from applications.models import Application
from .models import Payment
from .forms import PaymentForm



@login_required
def payment_page(request):
    application = get_object_or_404(Application, applicant=request.user)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.save()
            
            # Mark application as paid
            application = Application.objects.get(applicant=request.user)
            application.payment_completed = True
            application.save()

            return redirect('dashboard')  # Redirect to dashboard after payment
    else:
        form = PaymentForm()
    return render(request, 'payments/payment_page.html', {'form': form})


def payment_verify(request):
    reference = request.GET.get('reference')

    payment = get_object_or_404(Payment, reference=reference)

    if payment.verified:
        mark_application_as_paid(payment.application, reference)
        
        


def payment_success(request, application_id):
    application = Application.objects.get(application_id=application_id)
    application.is_paid = True
    application.save()
    return redirect('application_status')
        
        
    
        
        
        



