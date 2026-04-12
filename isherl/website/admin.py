from django.contrib import admin
from .models import About_Section_Five, Contact, ContactHeader, CourseDetails, CourseHeader, CourseList, EventHeader, EventList, HomeSlider, HomeSection_Two,HomeSection_Three, HomeSection_Four,Footer,About,About_Section_Two,About_Section_Three,About_Section_Four, NavLogo, Trainer


@admin.register(HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    list_display = ('title_one','description')
    
@admin.register(HomeSection_Two)
class HomeSection_TwoAdmin(admin.ModelAdmin):
   list_display = ('title','description')
   
@admin.register(HomeSection_Three)
class HomeSection_ThreeAdmin(admin.ModelAdmin):
   list_display = ('title','description')
   
@admin.register(HomeSection_Four)
class HomeSection_FourAdmin(admin.ModelAdmin):
   list_display = ('title','description')
   



@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
   list_display = ('title','description')
   
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
   list_display = ('title','description')
   
@admin.register(About_Section_Two)
class About_Section_TwoAdmin(admin.ModelAdmin):
   list_display = ('title','description')
   
   
@admin.register(About_Section_Three)
class About_Section_ThreeAdmin(admin.ModelAdmin):
   list_display = ('title','description')
   
@admin.register(About_Section_Four)
class About_Section_FourAdmin(admin.ModelAdmin):
   list_display = ('title','description')
   
   
@admin.register(About_Section_Five)
class About_Section_FiveAdmin(admin.ModelAdmin):
   list_display = ('title','description')   
   

   
@admin.register(CourseList)
class CourseListAdmin(admin.ModelAdmin):
   list_display = ('title','description')


@admin.register(CourseHeader)
class CourseHeaderAdmin(admin.ModelAdmin):
   list_display = ('header_title','header_description')
   
   
@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
   list_display = ('name','position')
   
    
   
   
@admin.register(EventList)
class EventListAdmin(admin.ModelAdmin):
   list_display = ('event_title','description')
   
@admin.register(EventHeader)
class EventHeaderAdmin(admin.ModelAdmin):
   list_display = ('header_title','header_description')
   
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
   list_display = ('name','office_one','office_two','office_three','office_four')
   
@admin.register(ContactHeader)
class ContactHeaderAdmin(admin.ModelAdmin):
   list_display = ('header_title','header_description')
   
   
@admin.register(NavLogo)
class NavLogoAdmin(admin.ModelAdmin):
   list_display = ('logo_name','logo_image')
   

   
   