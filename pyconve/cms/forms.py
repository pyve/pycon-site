#coding=utf-8
from django.contrib.auth.models import User
from localization.models import *
from django import forms

class RegistrationProfileForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['confirm_password']

        if password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        
        return password
    

class UserProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    country = forms.MultipleChoiceField(queryset=Country.objects.all())
    state = forms.MultipleChoiceField(queryset=State.objects.none())


class SpeakerProfileForm(forms.Form):
    """
    El avatar se podría gestionar con gravatar
    """
    about = forms.CharField(widget=forms.TextArea)


class PresentationForm(forms.Form):
    sepakers = forms.MultipleChoiceField(queryset=User.objects.all())
    name = forms.CharField(max_length=128)
    description = forms.CharField(widget=forms.TextArea)
    tutorial = forms.BooleanField()
    duration = forms.DecimalField()
    requirements = forms.CharField(widget=forms.TextArea)

