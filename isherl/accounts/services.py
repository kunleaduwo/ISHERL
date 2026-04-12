from accounts.models import EmailVerification
from django.conf import settings
from django.core.mail import send_mail

def send_email_verification(user):
    verification = EmailVerification.objects.create(user=user)
    verification_link = f"{settings.SITE_URL}/verify-email/{verification.token}/"

    send_mail(
        subject="Verify Your Email",
        message=f"Click this link to verify your email: {verification_link}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
    )
