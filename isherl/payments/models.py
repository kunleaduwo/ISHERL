from django.db import models
from django.conf import settings
from applications.models import Application

  
    
class Payment(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE,related_name='payment_appl_payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default="NGN")
    reference = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    payment_type = models.CharField(max_length=30,choices=[('application_fee', 'Application Fee'),('school_fee', 'School Fee')], blank=True)
    
    payment_status = models.CharField(
         max_length=20,
        choices=[
            ('select', 'Select'),
            ("pending", "Pending"),
            ("paid", "Paid"),
            ("failed", "Failed"),
        ],
    )
       
    paid_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)
    



