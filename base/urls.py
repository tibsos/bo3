from django.urls import path

from .views import *

app_name = 'base'

urlpatterns = [

    path('', landing, name = 'l'),

    #path('$/', payments_http),

    path('contact-us/', contact_us, name = 'contact-us'),
    path('contact/', contact, name = 'contact'),

    path('terms/', terms),
    path('privacy/', privacy),
    path('juridical-information/', juridical),

]