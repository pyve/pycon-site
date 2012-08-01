#coding=utf-8
from django.shortcuts import Render as Render
from django.contrib.auth.models import User
from django.contrib.auth.views import logout as auth_logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.utils import simplejson
from django.contrib.auth.decorators import login_required
from django.conf import settings
from profiles.models import *
from cms.models import Presentation
import hashlib
import base64
import datetime

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))

def profile_success(request):
    context = {'success_message': 'El perfil ha sido creado correctamente. Por favor revise su correo para validar el registro.'}
    return Render('base.html',RequestContext(request, context))

def profile_create(request):
    """
    GET: show profile creation form
    POST: validates and stores data
    """
    from profiles.forms import UserProfileForm
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user = User()
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.username = form.cleaned_data['email']
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password'])
            user.save()
            up = UserProfile.objects.get(user=user)
            up.country = form.cleaned_data['country']
            if form.cleaned_data.has_key('state'):
                up.state = form.cleaned_data['state']
            if form.cleaned_data.has_key('about'):
                up.about = form.cleaned_data['about']
            up.save()
            return HttpResponseRedirect(reverse('success-profile'))
        else:
            context = {'formUserProfile': form}
            return Render('base.html',RequestContext(request, context))
    return HttpResponseRedirect('/#inscriptions')

@login_required(login_url=settings.LOGIN_URL)
def profile_edit(request):
    """
    GET: show profile edit form with current data
    POST: validate and store new data
    """
    from profiles.forms import UserProfileForm
    profile = get404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['user_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_date['email']
            user.username = form.cleaned_date['email']
            user.set_password(form.cleaned_data['password'])
            up = UserProfile.objects.get(user=user)
            up.country = form.cleaned_data['country']
            up.state = form.cleaned_data['state']
            up.about = form.cleaned_data['about']
            user.save()
            up.save()
            context = {'status_message': 'Perfil actualizado'}
            return HttpResponse(simplejson.dumps(context))
        else:
            context = {'status_message': form.errors}
            return HttpResponse(status=400, content=simplejson.dumps(context))
    data = {
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
        'country': profile.country,
        'state': profile.state,
    }
    context = {'data': data}
    return Render('profiles/profile_create.html', RequestContext(request, context))

def profile_activate(request, encoded):
    try:
        regprofile = RegistrationProfile.objects.get(encoded=encoded)
        email, token = base64.b64decode(encoded).split('|')
        if (not regprofile.user.is_active) and email == regprofile.user.email and token == regprofile.token:
            regprofile.user.is_active = True
            regprofile.user.save()
            context = {'status_message': 'Perfil activate'}
            return Render('profiles/profile_activate.html', RequestContext(request, context))
    except:
        pass
    context = {'status_message': 'Usuario ya activado o token inválido'}
    return HttpResponse(status=403, content=simplejson.dumps(context))

def speaker_registration(request):
    if request.method == 'POST':
        from profiles.forms import SpeakerRegistrationForm
        form = SpeakerRegistrationForm(request.POST)
        if form.is_valid():
            user = User()
            user.first_name = form.cleaned_data['s_first_name']
            user.last_name = form.cleaned_data['s_last_name']
            user.username = form.cleaned_data['s_email']
            user.email = form.cleaned_data['s_email']
            user.set_password(form.cleaned_data['s_password'])
            user.save()
            up = UserProfile.objects.get(user=user)
            up.country = form.cleaned_data['s_country']
            if form.cleaned_data.has_key('s_state'):
                up.state = form.cleaned_data['s_state']
            up.about = form.cleaned_data['s_about']
            up.save()
            p = Presentation()
            p.name = form.cleaned_data['s_presentation_name']
            p.description = form.cleaned_data['s_presentation_description']
            p.tutorial = form.cleaned_data['s_presentation_tutorial']
            p.duration = form.cleaned_data['s_presentation_duration']
            p.requirements = forms.cleaned_data['s_presentation_requirements']
            p.save()
            p.speakers.add(user)
            p.save()
            return HttpResponseRedirect(reverse('success-profile'))
        else:
            context = {'formUserProfile': form}
            return Render('base.html',RequestContext(request, context))
    return HttpResponseRedirect('/#inscriptions')

@login_required(login_url=settings.LOGIN_URL)
def profiles_myprofile(request):
    from cms.forms import PresentationForm

    ps = request.user.presentation_set.all()
    context = {'data': ps}
    #return HttpResponse(simplejson.dumps(context))
    context = {'formSpeakerRegistration': PresentationForm(), 'ps': ps}
    return Render('profile.html', RequestContext(request, context))
