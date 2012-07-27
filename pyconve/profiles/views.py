#coding=utf-8
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.views import logout as auth_logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.utils import simplejson
from profiles.models import *
import hashlib
import base64
import datetime


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))


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
            context = {'status_message': 'Perfil creado', 'formUserProfile': form}
            return render_to_response('base.html',RequestContext(request, context))
            #return HttpResponse(simplejson.dumps(context))
        else:
            context = {'status_message': form.errors, 'formUserProfile': form}
            return render_to_response('base.html',RequestContext(request, context))
            #return HttpResponse(status=400, content=simplejson.dumps(context))
    form = UserProfileForm()
    context = {'form': form}
    return Render('profiles/create_profile.html', RequestContext(request, context))


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
