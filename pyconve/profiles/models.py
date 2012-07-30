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

    Los votos son para las ponencias, el workflow aun no se define

    El ponente es un usuario también, cualquier usuario puede proponer una
    charla.
    """
    user = models.OneToOneField(User)
    state = models.ForeignKey(State, blank=True, null=True) 
    country = models.ForeignKey(Country, blank=True, null=True)
    available_votes = models.IntegerField(default=5)
    picture = models.ImageField(upload_to='avatars', blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user

    def __unicode__(self):
        return u'%s'%self.user
    

SPONSORSHIP_CHOICES = (
    ('p', 'Plata'),
    ('g', 'Gold'),
    ('b', 'Bronce'),
    ('pl', 'Platino'),
)

class Sponsor(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    logo = models.ImageField(upload_to='logos', null=True, blank=True)
    website = models.URLField(max_length=256, null=True, blank=True)
    sponsorship_type = models.CharField(max_length=2, null=True, blank=True, choices=SPONSORSHIP_CHOICES)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s'%self.name

import profiles.signals
