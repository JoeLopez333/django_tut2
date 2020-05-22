from django.db.models.signals import post_save
from django.contrib.auth.models import User
#User model is 'sender'
from django.dispatch import receiver
#reciever
from .models import Profile

#we want a user profile to be created for each new user
@receiver(post_save, sender=User) #when a user is saved, send post_save signal to receiver
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User) #when a user is saved, send post_save signal to receiver
def save_profile(sender, instance, **kwargs): #kwargs accepts additional keyword args
    instance.profile.save()