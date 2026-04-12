
from django.utils import timezone
import uuid
from django.db import models
from accounts.models import CustomUser
from accounts import forms
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.conf import settings

User = settings.AUTH_USER_MODEL


TITLE_CHOICES = [
    ("mr", "Mr"),
    ("mrs", "Mrs"),
    ("dr", "Dr"),
    
]

GENDER_CHOICES = [
    ("male", "Male"),
    ("female", "Female"),
        
]


EMPLOYMENT_TYPE_CHOICES = [
    ("employed", "Employed"),
    ("self-employed", "Self-Employed"),
    ("unemployed", "Unemployed"), 
]


class Application(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('pending', 'pending'),
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    applicant = models.OneToOneField(CustomUser, on_delete=models.CASCADE,related_name='applications_as_applicant')
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='applications_as_user',blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="profile_pics/",  # folder inside MEDIA_ROOT
        blank=True,
        null=True
    )
    application_id = models.CharField(max_length=20, unique=True, blank=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    course_name = models.CharField(max_length=200,blank=True)
    department = models.CharField(max_length=200,blank=True)
    personal_info_completed = models.BooleanField(default=False)
    documents_uploaded = models.BooleanField(default=False)
    payment_completed = models.BooleanField(default=False)
    
    title = models.CharField(max_length=10, choices=TITLE_CHOICES, default='dr')
    first_name = models.CharField(max_length=150,blank=True)
    last_name = models.CharField(max_length=150,blank=True)
    middle_name = models.CharField(max_length=150,blank=True)
    
    father_name = models.CharField(max_length=150,blank=True)
    mother_name = models.CharField(max_length=150,blank=True)
    date_of_birth = models.DateField(blank=True,null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20,blank=True)
    
    program = models.CharField(max_length=150,blank=True)
    previous_school = models.CharField(max_length=255,blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    address = models.TextField(blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='male')
    
    nationality = models.CharField(max_length=100,blank=True)
    marital_status = models.CharField(max_length=100,blank=True)
    
    occupation = models.CharField(max_length=255,blank=True)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE_CHOICES, default='unemployed')
    office_address = models.CharField(max_length=300,blank=True)
    position_held = models.CharField(max_length=300,blank=True)
    company_name = models.CharField(max_length=300,blank=True)
    degree = models.CharField(max_length=300,blank=True)
    
   
    qualification =models.CharField(max_length=450,blank=True)
    institution_attended_line_one = models.CharField(max_length=450,blank=True)
    institution_attended_line_two = models.CharField(max_length=450,blank=True)
    institution_attended_line_three = models.CharField(max_length=450,blank=True)
    institution_attended_line_four = models.CharField(max_length=450,blank=True)
    additional_qualifications = models.TextField(max_length=1000,blank=True)
    date_of_award = models.DateField(blank=True,null=True)
    
    language =models.CharField(max_length=255,blank=True)
    grade = models.CharField(max_length=100,blank=True)
       
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    is_paid = models.BooleanField(default=False)
    todays_date = models.DateField(auto_now=True, editable=False)
   
    
    def generate_application_id(self):
        return f"APP-{uuid.uuid4().hex[:8].upper()}"

    def save(self, *args, **kwargs):
        # Ensure an applicant is set
        if not self.applicant_id:
            raise ValueError("Application must have an applicant")

        # Generate a unique application_id if it doesn't exist
        if not self.application_id:
            self.application_id = self.generate_application_id()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Application for {self.first_name} - {self.last_name} - {self.application_id} - {self.status}"
    


    
class ApplicationDocument(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name="documents")
    document_type = models.CharField(
        max_length=100,
        choices=[
            ('select', 'Select'),
            ("resume", "Resume"),
            ("passport", "Passport"),
            ("identity card", "Identity Card"),
            ("certificate", "Certificate"),
            ("registration payment slip", "Registration Payment Slip"),
            ("high school certificate", "High School Certificate"),
            ("transcript", "Transcript"),
            ("nin", "NIN"),
            
        ]
    )
    file = models.FileField(upload_to="documents/")
    uploaded_at = models.DateTimeField(default=timezone.now, editable=False)

   
    
class Title(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class ProfilePhoto(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_photos/")
    uploaded_at = models.DateTimeField(default=timezone.now, editable=False)
    
    

class Payment(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE,related_name='appl_payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default="NGN")
    reference = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)
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




class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    def __str__(self):
        return f"{self.user.email}'s profile"
    




    
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)











