from django.db import models
from accounts.models import CustomUser
from django.conf import settings
from applications.models import Application

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="student")
    student_id = models.CharField(max_length=20, unique=True)
    application = models.OneToOneField(Application, on_delete=models.CASCADE,blank=True,null=True)
    course_name = models.CharField(max_length=100,blank=True)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.student_id})"




