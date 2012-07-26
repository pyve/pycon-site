#coding=utf-8
from django.contrib.auth.models import User
from django.forms import forms
from localization.models import *
from profiles.models import *


class UserProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    country = forms.ModelChoiceField(queryset=Country.objects.all())
    state = forms.ModelChoiceField(queryse=State.objects.none())
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
    El avatar se podría gestionar con gravatar
    """
    class Meta:
        model = SpeakerProfile
