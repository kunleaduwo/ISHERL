from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser 
from django.contrib.auth.forms import AuthenticationForm 
from captcha.fields import CaptchaField


class CustomUserCreationForm(UserCreationForm):
    captcha = CaptchaField()
    phone_number = forms.CharField(max_length=15, required=False)
    address = forms.CharField(max_length=255, required=False)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'address', 'password1', 'password2','captcha')
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        
        
        
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
    remember_me = forms.BooleanField(required=False, initial=False)
    

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'address', 'password1', 'password2', )







