#coding=utf-8
from django.contrib.auth.models import User
from django.db import models
from localization.models import Country, State

class Presentation(models.Model):
    """
    Una ponencia la puede dar más de una persona
    por ello speakers es many2many

    El campo requirements debe activarse únicamente
    si la presentación es un tutorial (mesa de trabajo)
    a manera de saber si es necesario tener algún software
    instalado en los laboratorios.

    La duración creo que podría expresarse en minutos, por 
    eso la puse como integer
    """
    speakers = models.ManyToManyField(User)
    name = models.CharField(max_length=128)
    description = models.TextField()
    tutorial = models.BooleanField(default=False)
    duration = models.IntegerField(default=60)
    approved = models.BooleanField(default=False)
    votes = models.IntegerField(editable=False, default=0)
    requirements = models.TextField(blank=True, null=True)


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
    
