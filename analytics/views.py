from django.shortcuts import render, HttpResponse

from django.contrib.auth.models import User

from django_user_agents.utils import get_user_agent

from datetime import datetime as dt

def overview(request):
    
    return render(request, 'overview.html')

def record_session(request):
    
    if request.method == 'POST':
        
        path = request.POST.get('path')
        
        user_agent = get_user_agent(request)
        
        device = user_agent.is_mobile # mobile/not
        print(device)
        
        ip = request.POST.get('ip')
        
        if request.user.is_authenticated:
            
            user = User.objects.get(username = request.user.username)
            
        else:
            
            user = None
        
        # TIME
        start_time = request.POST.get('start_time')
        end_time = dt.now()
        print(start_time)
        print(end_time)
        session_duration = end_time - start_time
        print(session_duration)
    
    return HttpResponse('K')