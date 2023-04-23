from django.db import models as m


class Session(m.Model):
    
    path = m.TextField()
    
    # user info
        # user 
        # ip
        # country
        # city
        # browser
        # device
        
    # time
    start_time = m.DateTimeField()
    end_time = m.DateTimeField()
    duration = m.PositiveSmallIntegerField() # in seconds
    
    class Meta:
        
        ordering = ['-end_time']