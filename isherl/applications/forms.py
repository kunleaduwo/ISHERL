from django import forms
from .models import Application, ProfilePhoto

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['application_id','applicant', 'status']
        
        

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = "__all__"

        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "date_of_award": forms.DateInput(attrs={"type": "date"}),

            "address": forms.Textarea(attrs={"rows": 3}),
            "additional_qualifications": forms.Textarea(attrs={"rows": 5}),

            "first_name": forms.TextInput(attrs={"placeholder": "Type your first name"}),
            "middle_name": forms.TextInput(attrs={"placeholder": "Type your middle name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Type your last name"}),

            "email": forms.EmailInput(attrs={"placeholder": "Type your email"}),
            "phone_number": forms.TextInput(attrs={"placeholder": "Type your phone number"}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

        
class ProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['applicant', 'profile_picture']
        
        
        
        

        
        
      
