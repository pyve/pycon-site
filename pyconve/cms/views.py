#coding=utf-8
from django.shortcuts import render_to_response as Render, get_object_or_404 as get404
from django.temaplate import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import simplejson
from cms.utils import userprofile_create as create_profile
from cms.models import *
import base64
import datetime

def home(request):
	context = {}
	return Render('base.html', RequestContext(request, context))

def profile_create(request):
    if request.method == 'POST':
        form = RegistrationProfileForm(request.POST)
        contenxt = {}
        if form.is_valid():
            user_email = form.cleaned_data['email']
            passwd = form.cleaned_data['password']
            user = User(email=user_email)
            user.set_password(passwd)
            user.save()
            return HttpResponse(simplejson.dumps({'status_message': 'Profile created'}))
        else:
            context = {'errors': form.errors}
            return HttpResponse(status=400, content=simplejson.dumps(context))
    else:
        form = RegistrationProfileForm()
    context = {'form': form}
    return Render('cms/profile_create.html', RequestContext(request, context))


def profile_activate(request, token):
    try:
        regprofile = RegistrationProfile.objects.get(encoded=token)
        email, token = base64.b64decode(token).split('|')
        if (not regprofile.user.is_active) and email == regprofile.user.email and token == regprofile.token:
            regprofile.user.is_active = True
            regprofile.user.save()
            regprofile.consumed = datetime.datetime.now()
            regprofile.save()
            context = {'status_message': 'Usuario activado'}
            return HttpResponse(simplejson.dumps(context))
    except:
        pass

    context = {'status_message': 'Token inválido o ya consumido'}
    return HttpResponse(status=400, content=simplejson.dumps(context)) 


def profile_edit(request):
    try:
        request.user.userprofile
    except:
        create_profile(request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.username = form.cleaned_data['email']
            user.save()
            user.userprofile.country = form.cleaned_data['country']
            if form.cleaned_data['country'].lower() == "venezuela":
                user.userprofile.state = form.cleaned_data['state']
            user.userprofile.save()
            return HttpResponseRedirect(reverse('profile-myprofile'))
        else:
            return HttpResponse(status=400, content=simplejson.dumps({'status_message': form.errors}))
    else:
        data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'country': request.user.userprofile.country,
            'state': request.user.userprofile.state,
        }
        form = UserProfileForm(data)
    context = {'form': form}
    return Render('cms/profile_edit.html', RequestContext(request, context))
