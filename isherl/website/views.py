from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from .models import About_Section_Five, Contact, ContactHeader, CourseDetails,CourseHeader, CourseList, EventHeader, EventList, HomeSlider,HomeSection_Two,HomeSection_Three, HomeSection_Four,Footer,About,About_Section_Two,About_Section_Three,About_Section_Four, NavLogo, Trainer


id = 1

def home(request):
    homesliders = HomeSlider.objects.all()
    homesectiontwo = HomeSection_Two.objects.all()
    homesectionthree = HomeSection_Three.objects.all()
    homesectionfour = HomeSection_Four.objects.all()
    footers = Footer.objects.all()
    
    return render(request, 'website/index.html', {
        
        'homesliders':homesliders,
        'homesectiontwo':homesectiontwo,
        'homesectionthree':homesectionthree,
        'homesectionfour':homesectionfour,
        'footers':footers,
        
        
        })



def about(request):
    aboutus = About.objects.all()
    section_two = About_Section_Two.objects.all()
    section_three = About_Section_Three.objects.all()
    section_four = About_Section_Four.objects.all()
    section_five = About_Section_Five.objects.all()
    
    
    return render(request, 'website/about.html',{
        'aboutus': aboutus,
        'section_two':section_two,
        'section_three':section_three,
        'section_four':section_four,
        'section_five':section_five,
        
    })

def course_list(request):
    courses = CourseList.objects.all()
    courseheaders = CourseHeader.objects.all()
    return render(request, 'website/courses.html', {
        'courses': courses,
        'courseheaders':courseheaders,
    })
    
    
def course_detail(request, pk):
    course = get_object_or_404(CourseList, pk=pk)

    return render(request, 'website/course-details.html', {
        'course': course,
       
    })
    
def navlogo(request):
    logo = NavLogo.objects.all()
    
    return render(request, 'base.html', {
        'logo':logo
    })
    
    

def trainers(request):
    trainers = Trainer.objects.all()
    return render(request, 'website/trainers.html', {
        'trainers': trainers
    })

def event_list(request):
    events = EventList.objects.all()
    eventsheader = EventHeader.objects.all()
    return render(request, 'website/events.html', {
        'events': events,
        'eventsheader':eventsheader,
        
    })
    
def event_detail(request, pk):
    event = get_object_or_404(EventList, pk=pk)

    return render(request, 'website/event-details.html', {
        'event': event,
       
    })    


def publications(request):
    return render(request, 'website/publications.html')

def blog(request):
    return render(request, 'website/blog.html')

def contact(request):
    contact = Contact.objects.all()
    contactheader = ContactHeader.objects.all()
    return render(request, 'website/contact.html', {
        'contact':contact,
        'contactheader':contactheader
    })



#dashboard

@login_required
def applicant_dashboard(request):
    return render(request, 'dashboard/applicant/dashboard.html')

@login_required
def student_dashboard(request):
    return render(request, 'dashboard/student/dashboard.html')










