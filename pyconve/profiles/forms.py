#coding=utf-8
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
from localization.models import *
from profiles.models import *


class UserProfileForm(forms.Form):
    first_name = forms.CharField(label="Nombres",max_length=30)
    last_name = forms.CharField(label="Apellidos",max_length=30)
    email = forms.EmailField(label="Correo")
    country = forms.ModelChoiceField(label="País", queryset=Country.objects.all())
    state = forms.ModelChoiceField(label="Estado", queryset=State.objects.all(), required=False)
    password = forms.CharField(label="Contraseña", required=True, widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirmar Contraseña", required=True, widget=forms.PasswordInput)

    def clean_password(self):
        
        if self.data['password'] != self.data['confirm_password']:
            raise forms.ValidationError('Las contraseñas ingresadas no coinciden. Por favor verifique.')

        return self.cleaned_data['password']

    def clean_email(self):
        if User.objects.filter(email=self.data['email']):
            raise forms.ValidationError('Este email ya se encuentra registrado. Por favor verifique.')
        return self.data['email']


class SpeakerRegistrationForm(forms.Form):
    s_first_name = forms.CharField(label="Nombres", max_length=30)
    s_last_name = forms.CharField(label="Apellidos", max_length=30)
    s_email = forms.EmailField(label='Correo')
    s_country = forms.ModelChoiceField(label='País', queryset=Country.objects.all())
    s_state = forms.ModelChoiceField(label='Estado', queryset=State.objects.all())
    s_about = forms.CharField(label='Acerca de mí', widget=forms.Textarea)
    s_password = forms.CharField(label='Contraseña', required=True, widget=forms.PasswordInput)
    s_confirm_password = forms.CharField(label='Confirmar Contraseña', required=True, widget=forms.PasswordInput)
    s_presentation_name = forms.CharField(label='Nombre de la presentación', max_length=128)
    s_presentation_description = forms.CharField(label='Descripción', widget=forms.Textarea)
    s_presentation_tutorial = forms.BooleanField(label='Tutorial/Mesa de Trabajo')
    s_presentation_duration = forms.IntegerField(label='Duranción (minutos)')
    s_presentation_requirements = forms.CharField(label='Requerimientos adicionales', widget=forms.Textarea)

    def clean_password(self):
        
        if self.data['password'] != self.data['s_confirm_password']:
            raise forms.ValidationError('Las contraseñas ingresadas no coinciden. Por favor verifique.')

        return self.cleaned_data['s_password']

    def clean_email(self):
        if User.objects.filter(email=self.data['s_email']):
            raise forms.ValidationError('Este email ya se encuentra registrado. Por favor verifique.')
        return self.data['s_email']


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(wiget=forms.PasswordInput)
