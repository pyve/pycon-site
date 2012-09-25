#coding=utf-8
from __future__ import unicode_literals
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
    requirements = models.TextField(blank=True, null=True)
    duration = models.IntegerField(default=60)
    tutorial = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    votes = models.IntegerField(editable=False, default=0)

    def __unicode__(self):
        return self.name
