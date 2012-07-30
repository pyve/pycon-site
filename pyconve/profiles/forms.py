#coding=utf-8
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
from localization.models import *
from profiles.models import *


class UserProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30, widget=widgets.TextInput(attrs={
        #'required': 'required'
        }))
    last_name = forms.CharField(max_length=30, widget=widgets.TextInput(attrs={
        #'required': 'required'
        }))
    email = forms.EmailField(widget=widgets.TextInput(attrs={
        #'type': 'email'
        }))
    country = forms.ModelChoiceField(queryset=Country.objects.all())
    state = forms.ModelChoiceField(queryset=State.objects.all())
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        #'required': 'required'
        }))
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        #'required': 'required'
        }))

    def clean_password(self):
        
        if self.data['password'] != self.data['confirm_password']:
            raise forms.ValidationError('Las contraseñas ingresadas no coinciden. Por favor verifique.')

        return self.cleaned_data['password']

    def clean_email(self):
        if User.objects.filter(email=self.data['email']):
            raise forms.ValidationError('Este email ya se encuentra registrado. Por favor verifique.')
        return self.data['email']


class SpeakerRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    country = forms.ModelChoiceField(queryset=Country.objects.all())
    state = forms.ModelChoiceField(queryset=State.objects.all())
    about = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput)
    presentation_name = forms.CharField(max_length=128)
    presentation_description = forms.CharField(widget=forms.Textarea)
    presentation_tutorial = forms.BooleanField()
    presentation_duration = forms.IntegerField()
    presentation_requirements = forms.CharField(widget=forms.Textarea)

    def clean_password(self):
        
        if self.data['password'] != self.data['confirm_password']:
            raise forms.ValidationError('Las contraseñas ingresadas no coinciden. Por favor verifique.')

        return self.cleaned_data['password']

    def clean_email(self):
        if User.objects.filter(email=self.data['email']):
            raise forms.ValidationError('Este email ya se encuentra registrado. Por favor verifique.')
        return self.data['email']


