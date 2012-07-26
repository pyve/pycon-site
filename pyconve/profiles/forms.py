#coding=utf-8
from django.contrib.auth.models import User
from django import forms
from localization.models import *
from profiles.models import *


class RegistrationProfileForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['confirm_password']

        if password != password2:
            raise forms.ValidationError('Las contrasenas no coinciden')
        
        return password
    

class UserProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    country = forms.ModelChoiceField(queryset=Country.objects.all())
    state = forms.ModelChoiceField(queryset=State.objects.none())
    password = forms.CharField(max_length=16, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=16, widget=forms.PasswordInput)

    def clean_password(self):
        pwd = self.cleaned_data['password']
        pwd2 = self.cleaned_data['confirm_password']
        
        if pwd1 != pwd2:
            raise forms.ValidateError('Las claves no contraseñas no coinciden')

        return pwd

class SpeakerProfileForm(forms.ModelForm):
    """
    El avatar se podria gestionar con gravatar
    """
    class Meta:
        model = SpeakerProfile
