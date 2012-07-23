from django.contrib.auth.models import User
from django.db import models
from localization.models import Country, State

class Presentation(models.Model):
    speakers = models.ManyToManyField(User)
    name = models.CharField(max_length=128)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    votes = models.IntegerField(editable=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    state = models.ForeignKey(State, blank=True, null=True) 
    country = models.ForeignKey(Country)
    email = models.EmailField()

class SpeakerProfile(UserProfile):
    picture = models.ImageField(upload_to='avatars', blank=True, null=True)
    about = models.TextField()
    
