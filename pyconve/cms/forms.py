#coding=utf-8
from django.contrib.auth.models import User
from localization.models import *
from cms.models import Presentation
from django import forms


class PresentationForm(forms.ModelForm):
    class Meta:
        model = Presentation
        exclude = ('votes', 'approved')
