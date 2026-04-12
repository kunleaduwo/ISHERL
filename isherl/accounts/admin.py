from django.contrib import admin
from .models import CustomUser
from .utils import convert_applicant_to_student

@admin.action(description="Approve applicant → Student")
def approve_as_student(modeladmin, request, queryset):
    for user in queryset.filter(is_applicant=True):
        convert_applicant_to_student(user)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", "is_applicant", "is_student", "is_active")
    list_filter = ("is_applicant", "is_student", "is_active")
    actions = [approve_as_student]

