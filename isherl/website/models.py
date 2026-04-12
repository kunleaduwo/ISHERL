from django.db import models





REGISTRATION_STATUS_CHOICES = [
    ('OPEN', 'Open'),
    ('CLOSED', 'Closed')
]



class NavLogo(models.Model):
    logo_name = models.CharField(max_length=400)
    logo_image = models.ImageField(upload_to='images/', default="none") 
    
    def __str__(self):
        return self.logo_name 



class HomeSlider(models.Model):
    title_one = models.CharField(max_length=200)
    title_two = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    background = models.ImageField(upload_to='images/', default="none") 
    
    def __str__(self):
        return self.title_one 
    
class HomeSection_Two(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=850)
    text_one = models.TextField(max_length=300)
    text_two = models.TextField(max_length=300)
    text_three = models.TextField(max_length=300)
    right_image = models.ImageField(upload_to='images/', default="none") 
    
    def __str__(self):
        return self.title 
    
class HomeSection_Three(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=400)
    subtitle_one = models.CharField(max_length=100)
    description_one = models.TextField(max_length=400)
    subtitle_two = models.CharField(max_length=100)
    description_two = models.TextField(max_length=400)
    subtitle_three = models.CharField(max_length=100)
    description_three = models.TextField(max_length=400)
    
    def __str__(self):
        return self.title
    
class HomeSection_Four(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300, default="none")
    feature_one = models.CharField(max_length=100)
    feature_two = models.CharField(max_length=100)
    feature_three = models.CharField(max_length=100)
    feature_four = models.CharField(max_length=100)
    feature_five = models.CharField(max_length=100)
    feature_six = models.CharField(max_length=100)
    feature_seven = models.CharField(max_length=100)
    feature_eight = models.CharField(max_length=100)
    feature_nine = models.CharField(max_length=100)
    feature_ten = models.CharField(max_length=100)
    feature_eleven = models.CharField(max_length=100)
    feature_twelve = models.CharField(max_length=100)

    
    def __str__(self):
        return self.title
    
class Footer(models.Model):
    title = models.CharField(max_length=100)
    footer_image = models.ImageField(upload_to='images/', default="none") 
    description = models.TextField(max_length=100)
    address_one = models.CharField(max_length=100, default="")
    address_two = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, default="")
    
    menu_two_title = models.CharField(max_length=100)
    menu_two_link_one = models.CharField(max_length=100)
    menu_two_link_two = models.CharField(max_length=100)
    menu_two_link_three = models.CharField(max_length=100)
    menu_two_link_four = models.CharField(max_length=100)
    menu_two_link_five = models.CharField(max_length=100)
    
    menu_three_title = models.CharField(max_length=100)
    menu_three_link_one = models.CharField(max_length=100)
    menu_three_link_two = models.CharField(max_length=100)
    menu_three_link_three = models.CharField(max_length=100)
    menu_three_link_four = models.CharField(max_length=100)
    menu_three_link_five = models.CharField(max_length=100)
    
    menu_four_title = models.CharField(max_length=100)
    footer_four_image = models.ImageField(upload_to='images/', default="none") 
    
    def __str__(self):
        return self.title
    
class About(models.Model):
    title = models.CharField(max_length=100) 
    description = models.TextField(max_length=850,blank=True)
    header_background = models.ImageField(upload_to='images/', default="none")
    
    def __str__(self):
        return self.title
    
class About_Section_Two(models.Model):
    title = models.CharField(max_length=200) 
    description = models.TextField(max_length=1000)
    about_page_image = models.ImageField(upload_to='images/', default="none")
    
    def __str__(self):
        return self.title
     
class About_Section_Three(models.Model):
    title = models.CharField(max_length=200) 
    description = models.TextField(max_length=1000)
    about_page_image_two = models.ImageField(upload_to='images/', default="none")
    
    def __str__(self):
        return self.title
     
class About_Section_Four(models.Model):
    title = models.CharField(max_length=200) 
    description = models.TextField(max_length=1000)
    about_page_image_three = models.ImageField(upload_to='images/', default="none")
    
    def __str__(self):
        return self.title

class About_Section_Five(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=600)
    subtitle_one = models.CharField(max_length=100)
    description_one = models.TextField(max_length=600)
    subtitle_two = models.CharField(max_length=100)
    description_two = models.TextField(max_length=600)
    subtitle_three = models.CharField(max_length=100)
    description_three = models.TextField(max_length=600)
    
    def __str__(self):
        return self.title

class Trainer(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=150)
    trainer_info = models.CharField(max_length=500)
    trainer_photo = models.ImageField(upload_to='images/', default="none")
    
    def __str__(self):
        return self.name

class CourseList(models.Model):
    title = models.CharField(max_length=200) 
    description = models.TextField(max_length=800)
    course_image = models.ImageField(upload_to='images/',blank=True)
    category = models.CharField(max_length=200,blank=True)
    course_trainer_name = models.CharField(max_length=200,blank=True)
    course_trainer_image = models.ImageField(upload_to='images/', default="none") 
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    
    header_title = models.CharField(max_length=200) 
    header_description = models.TextField(max_length=500)
    
    course_heading = models.CharField(max_length=200)
    course_info = models.TextField(max_length= 1000,blank=True)
    course_info_two = models.TextField(max_length=1000,blank=True)
    course_info_three = models.TextField(max_length=1000,blank=True)
    course_info_four = models.TextField(max_length=1000,blank=True)
    course_info_five = models.TextField(max_length=1000,blank=True)
  
    
    left_tab_one = models.CharField(max_length=100,blank=True)
    tab_subheading_one = models.CharField(max_length=200,blank=True)
    tab_description_one_a = models.TextField(max_length=800,blank=True)
    tab_description_one_b= models.TextField(max_length=800,blank=True)
    buttom_right_image_one = models.ImageField(upload_to='images/', default="none")

    left_list_tab_two = models.CharField(max_length=100,blank=True)
    tab_subheading_two = models.CharField(max_length=200,blank=True)
    tab_description_two_a = models.TextField(max_length=800,blank=True)
    tab_description_two_b= models.TextField(max_length=800,blank=True)
    buttom_right_image_two = models.ImageField(upload_to='images/', default="none")
    
    left_list_tab_three = models.CharField(max_length=100,blank=True)
    tab_subheading_three = models.CharField(max_length=200,blank=True)
    tab_description_three_a = models.TextField(max_length=800,blank=True)
    tab_description_three_b= models.TextField(max_length=800,blank=True)
    buttom_right_image_three = models.ImageField(upload_to='images/', default="none")
    
    left_list_tab_four = models.CharField(max_length=100,blank=True)
    tab_subheading_four = models.CharField(max_length=200,blank=True)
    tab_description_four_a = models.TextField(max_length=800,blank=True)
    tab_description_four_b= models.TextField(max_length=800,blank=True)
    buttom_right_image_four = models.ImageField(upload_to='images/', default="none")
    
    left_list_tab_five = models.CharField(max_length=100,blank=True)
    tab_subheading_five = models.CharField(max_length=200,blank=True)
    tab_description_five_a = models.TextField(max_length=800,blank=True)
    tab_description_five_b= models.TextField(max_length=800,blank=True)
    buttom_right_image_five = models.ImageField(upload_to='images/', default="none")
    
    right_list_header = models.CharField(max_length=100)
    course_fee = models.CharField(max_length=100)
    duration = models.CharField(max_length=100,blank=True)
    start_date = models.DateField( blank=True)
    end_date = models.DateField(blank=True)
    
    application_procedure = models.TextField(max_length=800,blank=True)
    language = models.CharField(max_length=100)
    certificate = models.CharField(max_length=600,blank=True)
    additional_info = models.TextField(max_length=700,blank=True)
    contact_email_address = models.EmailField(blank=True)
    registration_date = models.DateField(blank=True)
    registration_status = models.CharField(
        max_length=6,
        choices=REGISTRATION_STATUS_CHOICES,
        default='OPEN',
    )
    
    def __str__(self):
        return self.title
      
class CourseDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.ForeignKey(CourseList, on_delete=models.DO_NOTHING,blank=True)
    course_image = models.ImageField(upload_to='images/',blank=True)
       
    
    def __str__(self):
        return self.header_title

class CourseHeader(models.Model):
    header_title = models.CharField(max_length=200, default="none")
    header_description = models.TextField(max_length=600, default="none")
    
    def __str__(self):
        return self.header_title
    
    

class EventList(models.Model):
    event_title = models.CharField(max_length=300) 
    description = models.TextField(max_length=800)
    event_image = models.ImageField(upload_to='images/', default="none")
    event_date = models.DateTimeField()
    
    page_header_title = models.CharField(max_length=300) 
    page_header_description = models.TextField(max_length=500)
    
    event_theme = models.TextField(max_length=500,blank=True)
    
    event_heading = models.CharField(max_length=300)
    event_details_one = models.TextField(max_length=850,blank=True)
    event_details_two = models.TextField(max_length=850,blank=True)
    event_details_three = models.TextField(max_length=850,blank=True)
    event_details_four = models.TextField(max_length=850,blank=True)
    event_details_five = models.TextField(max_length=850,blank=True)
     
 
    chairpersons = models.TextField(max_length=300,blank=True) 
   
    
    speakers= models.TextField(max_length=700,blank=True)
     
    left_tab_one = models.CharField(max_length=100,blank=True)
    tab_subheading_one = models.CharField(max_length=200,blank=True)
    tab_description_one_a = models.TextField(max_length=800,blank=True)
    tab_description_one_b= models.TextField(max_length=800,blank=True)
    buttom_right_image_one = models.ImageField(upload_to='images/',blank=True)

    left_list_tab_two = models.CharField(max_length=100,blank=True)
    tab_subheading_two = models.CharField(max_length=200,blank=True)
    tab_description_two_a = models.TextField(max_length=800,blank=True)
    tab_description_two_b= models.TextField(max_length=800,blank=True)
    buttom_right_image_two = models.ImageField(upload_to='images/',blank=True)
    
    left_list_tab_three = models.CharField(max_length=100,blank=True)
    tab_subheading_three = models.CharField(max_length=200,blank=True)
    tab_description_three_a = models.TextField(max_length=800,blank=True)
    tab_description_three_b= models.TextField(max_length=800,blank=True)
    buttom_right_image_three = models.ImageField(upload_to='images/',blank=True)
    
    left_list_tab_four = models.CharField(max_length=100,blank=True)
    tab_subheading_four = models.CharField(max_length=200,blank=True)
    tab_description_four_a = models.TextField(max_length=800,blank=True)
    tab_description_four_b= models.TextField(max_length=800,blank=True)
    buttom_right_image_four = models.ImageField(upload_to='images/',blank=True)
    
    left_list_tab_five = models.CharField(max_length=100,blank=True)
    tab_subheading_five = models.CharField(max_length=200,blank=True)
    tab_description_five_a = models.TextField(max_length=800,blank=True)
    tab_description_five_b= models.TextField(max_length=800,blank=True)
    buttom_right_image_five = models.ImageField(upload_to='images/',blank=True)
    
    right_list_header = models.CharField(max_length=100)
    event_venue = models.CharField(max_length=400)
    event_fee = models.CharField(max_length=100)
    duration = models.CharField(max_length=100,blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    
    additional_information = models.TextField(max_length=800,blank=True)
    contact_phone_number = models.CharField(max_length=50,blank=True)
    contact_email_address = models.EmailField(blank=True)
    registration_date = models.DateField()
    registration_status = models.CharField(
        max_length=6,
        choices=REGISTRATION_STATUS_CHOICES,
        default='OPEN',
    )
    
    def __str__(self):
        return self.event_title
    
class EventHeader(models.Model):
    header_title = models.CharField(max_length=200,blank=True)
    header_description = models.TextField(max_length=600,blank=True)
    
    def __str__(self):
        return self.header_title
  
class EventDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    event = models.ForeignKey(EventList, on_delete=models.DO_NOTHING,blank=True)
    event_image = models.ImageField(upload_to='images/',blank=True)  


class ContactHeader(models.Model):
    header_title = models.CharField(max_length=200,blank=True)
    header_description = models.TextField(max_length=600,blank=True)
    
    def __str__(self):
        return self.header_title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    office_one = models.CharField(max_length=250,blank=True)
    address_one = models.CharField(max_length=250,blank=True) 
    phone_one = models.CharField(max_length=250,blank=True)
    email_one = models.EmailField(max_length=250,blank=True)
    
    office_two = models.CharField(max_length=250,blank=True)
    address_two = models.CharField(max_length=250,blank=True) 
    phone_two = models.CharField(max_length=250,blank=True)
    email_two = models.EmailField(max_length=250,blank=True)
    
    office_three = models.CharField(max_length=250,blank=True)
    address_three = models.CharField(max_length=250,blank=True) 
    phone_three = models.CharField(max_length=250,blank=True)
    email_three = models.EmailField(max_length=250,blank=True)
    
    office_four = models.CharField(max_length=250,blank=True)
    address_four = models.CharField(max_length=250,blank=True) 
    phone_four = models.CharField(max_length=250,blank=True)
    email_four = models.EmailField(max_length=250,blank=True)
    
    def __str__(self):
        return self.name
        
    

    
    
    
    