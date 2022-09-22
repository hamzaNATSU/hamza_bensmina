from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import Profile



def create_profile(sender , **kwargs):
    if kwargs["created"]:
        user_profile = Profile.objects.create(user=kwargs['instance'])
    
post_save.connect(create_profile , sender=User)