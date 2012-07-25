#coding=utf-8
from django.contrib.auth.models import User
from django.db import models
from localization.models import *


class RegistrationProfile(models.Model):
    user = models.OneToOneField(User)
    token = models.CharField(max_length=32)
    encoded = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now_add=True)
    consumed = models.DateTimeField(null=True, blank=True)
    

class UserProfile(models.Model):
    """
    Simplemente para tener una idea de la cantidad de 
    personas que vienen del interior

    Los votos son para las ponencias, el workflow 
    """
    user = models.OneToOneField(User)
    state = models.ForeignKey(State, blank=True, null=True) 
    country = models.ForeignKey(Country)
    available_votes = models.IntegerField(default=5)


class SpeakerProfile(UserProfile):
    """
    Se agrega una biografía y una fotito al UserProfile
    para los ponentes, a manera de que la audiencia pueda
    tener una idea de a quienes van a ver
    """
    picture = models.ImageField(upload_to='avatars', blank=True, null=True)
    about = models.TextField()

