
# from django.contrib import admin
# from .models import Application
# from .services import accept_application

# @admin.register(Application)
# class ApplicationAdmin(admin.ModelAdmin):
#     list_display = ('user','application_id', 'status','is_paid')
#     list_filter = ('status', 'is_paid')
#     actions = ['accept_selected']
    

#     def accept_selected(self, request, queryset):
#         for application in queryset:
#             accept_application(application)

#     accept_selected.short_description = "Accept selected applications"



from django.contrib import admin
from .models import Application
from students.utils import create_student_from_application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('application_id', 'first_name','last_name', 'status', 'is_paid')
    list_filter = ('status', 'is_paid')

    def save_model(self, request, obj, form, change):
        old_status = None
        if obj.pk:
            old_status = Application.objects.get(pk=obj.pk).status

        super().save_model(request, obj, form, change)

        if obj.status == 'approved' and old_status != 'approved':
            create_student_from_application(obj)
