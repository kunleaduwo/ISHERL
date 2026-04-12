from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from two_factor.urls import urlpatterns as tf_urls


urlpatterns = [
    
    path("admin/", admin.site.urls),
    path('', include(tf_urls)),
    path('accounts/',include('accounts.urls')),
    path('',include('website.urls')),# I used this for CAPTCHA verification URL
    
    #path('accounts/', include('two_factor.urls', 'two_factor')),
    
    
    path('payments/',include('payments.urls')),
    path('applications/',include('applications.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('students/',include('students.urls')),   

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
    


