from django.shortcuts import render, HttpResponse

from .models import Message

from datetime import datetime as dt

from django_user_agents.utils import get_user_agent

def landing(request):
    
    c = {}
    
    c['user'] = request.user
    c['start_time'] = dt.now()
    c['ip'] = request.META.get('REMOTE_ADDR')
    

    return render(request, 'landing.html', c)

# Contact

def contact_us(request):

    c = {}

    c['user'] = request.user
    
    if request.user.is_authenticated:
        
        c['name'] = request.user.profile.name
        
    return render(request, 'contact.html', c)
    
# contact submit
def contact(request):
    
    if request.user.is_authenticated:
        
        Message.objects.create(
            
            user = request.user,

            topic = request.POST.get('t'),
            message = request.POST.get('m'),
            
        )
        
    else:
        
        Message.objects.create(
            
            name = request.POST.get('n'),
            email = request.POST.get('e'),
            
            topic = request.POST.get('t'),
            message = request.POST.get('m'),

        )
    
    return HttpResponse('K')

# Info

def terms(request):

    return render(request, 'info/terms.html', {'user': request.user})

def privacy(request):

    return render(request, 'info/privacy.html', {'user': request.user})

def juridical(request):

    return render(request, 'info/juridical.html', {'user': request.user})
