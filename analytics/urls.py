from django.urls import path

from .views import *

app_name = 'analytics'

urlpatterns = [
    
    path('overview', overview),
    
    path('record_session/', record_session, name = 'record-session'),
    
]