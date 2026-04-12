from django.db import transaction
from .models import Payment

@transaction.atomic
def mark_application_as_paid(payment: Payment):
    application = payment.application  # no direct import needed

    if application.payment_completed:
        return  # prevent double processing

    payment.verified = True
    payment.save()

    application.payment_completed = True
    application.save()
