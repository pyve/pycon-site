#coding=utf-8
from django.contrib.auth.models import User
from localization.models import *
from django import forms


class PresentationForm(forms.Form):
    speakers = forms.MultipleChoiceField(choices=User.objects.all())
    name = forms.CharField(max_length=128)
    description = forms.CharField(widget=forms.Textarea)
    tutorial = forms.BooleanField()
    duration = forms.DecimalField()
    requirements = forms.CharField(widget=forms.Textarea)

