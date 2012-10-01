#coding=utf-8
from django.shortcuts import render_to_response as Render, get_object_or_404 as get404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import simplejson
from django.contrib.auth.decorators import login_required
from django.conf import settings
from cms.models import *
from cms.forms import PresentationForm

def home(request):
    from profiles.forms import UserProfileForm, PasswordRecoveryForm
    context = {'formUserProfile': UserProfileForm(), 'passwordRecoveryForm': PasswordRecoveryForm()}
    return Render('base.html', RequestContext(request, context))

def presentation_success(request):
    from cms.forms import PresentationForm
    ps = request.user.presentation_set.all()
    context = {'success_message': 'La presentación ha sido creado correctamente.', 'ps':ps, 'formSpeakerRegistration': PresentationForm() }
    return Render('profile.html',RequestContext(request, context))

@login_required(login_url=settings.LOGIN_URL)
def presentation_create(request):
    """
    GET: shows the presentation registration form
    POST: saves all the information
    """
    from cms.forms import PresentationForm
    context = {}
    if request.method == 'POST':
        form = PresentationForm(request.POST)
        if form.is_valid():
            p = Presentation()
            p.name = form.cleaned_data['name']
            p.description = form.cleaned_data['description']
            p.tutorial = form.cleaned_data['tutorial']
            p.duration = form.cleaned_data['duration']
            p.requirements = form.cleaned_data['requirements']
            p.save()
            p.speakers.add(request.user)
            p.save()
            context = {'status_message': 'Charla creada'}
            #return Render('profile.html',RequestContext(request, context))
            return HttpResponseRedirect(reverse('success-presentation'))
            #return HttpResponse(simplejson.dumps(context))
        else:
            context = {'status_message': form.errors}
            return HttpResponse(status=400, content=simplejson.dumps(context))
    else:
        context = {'form': PresentationForm()}
    return Render('cms/presentation_create.html', RequestContext(request, context))


def presentation_list(request):
    context = {}
    return Render('presentation_list.html', RequestContext(request, context))


def presentation_view(request, presentation_id):
    import hashlib
    from profiles.models import UserProfile
    p = get404(Presentation, id=presentation_id)
    s = p.speakers.all()[0]
    profile = UserProfile.objects.get(user=s)
    context = {
        'avatar':'http://www.gravatar.com/avatar/%s'%hashlib.md5(s.email).hexdigest(),
        'presentation': p,
        'speaker': s.get_full_name(),
        'about': profile.about,
        'country': profile.country,
        'state': profile.state,
    }
    return Render('presentation_detail.html', RequestContext(request, context))

@login_required(login_url=settings.LOGIN_URL)
def presentation_edit(request, presentation_id):
    """
    GET: show the presentation edit form
    POST: validates and saves all the information
    """
    from cms.forms import PresentationForm
    context = {}
    p = get404(Presentation, id=presentation_id)
    if request.method == 'POST':
        form = PresentationForm(request.POST) 
        if form.is_valid():
            #form.save()
            p.name = form.cleaned_data['name']
            p.description = form.cleaned_data['description']
            p.tutorial = form.cleaned_data['tutorial']
            p.duration = form.cleaned_data['duration']
            p.requirements = form.cleaned_data['requirements']
            p.save()
            ps = request.user.presentation_set.all()
            context = {'ps': ps, 'formSpeakerRegistration' : PresentationForm()}
            return HttpResponseRedirect(reverse('my-profile'))
            # return Render('profile.html',RequestContext(request, context))

            # context = {'status_message': 'Cambios realizados'}
            # return HttpResponse(simplejson.dumps(context))
            # if request.user in p.speakers.all():
            #     #p.speakers = form.cleaned_data['speakers']
            #     p.name = form.cleaned_data['name']
            #     p.description = form.cleaned_nada['description']
            #     p.tutorial = form.cleaned_data['tutorial']
            #     p.duration = form.cleaned_data['duration']
            #     p.requirements = form.cleaned_data['requirements']
            #     p.save()
            #     context = {'status_message': 'Cambios realizados'}
            #     return HttpResponse(simplejson.dumps(context))
            # else:
            #     context = {'status_message': 'Debes ser uno de los ponentes para editar la charla'}
            #     return HttpResponse(status=403, content=context)
        else:
            context = {'status_message': form.errors}
            return HttpResponse(status=400, content=simplejson.dumps(context))
    else:
        
        elemento = Presentation.objects.get(id=int(presentation_id))
        form = PresentationForm(instance=elemento)
        context = { 'formSpeakerRegistration' : form, 'presentation_id':elemento.id}
        data = {
            'speakers': p.speakers.all(),
            'name': p.name,
            'description': p.description,
            'tutorial': p.tutorial,
            'duration': p.duration,
            'requirements': p.requirements,
        }
        #ps = request.user.presentation_set.all()
        #context = {'data': data}
    return Render('_presentation.html', RequestContext(request, context))


@login_required(login_url=settings.LOGIN_URL)
def presentation_vote(request, presentation_id):
    context = {}
    if request.method == 'POST':
        p = get404(Presentation, id=presentation_id)
        p.votes += 1
        p.save()
        context = {'status_message': 'Voto agregado con éxito'}
        return HttpResponse(simplejson.dumps(context))
    return HttpResponse(status=405)


@login_required(login_url=settings.LOGIN_URL)
def my_presentations(request):
    ps = request.user.presentation_set.all()
    context = {'data': ps}
    return HttpResponse(simplejson.dumps(context))

@login_required(login_url=settings.LOGIN_URL)
def presentation_delete(request, presentation_id):
    p = get404(Presentation, id=presentation_id)
    if request.method == 'POST':
        #p = get404(Presentation, id=presentation_id)
        if request.user in p.speakers.all():
            p.delete()
        else:
            context = {'status_message': 'Esta presentación no es tuya'}
            return HttpResponse(status=403, content=context)
        return HttpResponse(status=200)
    else:
        p.delete()
        ps = request.user.presentation_set.all()
        context = {'ps': ps, 'formSpeakerRegistration' : PresentationForm()}
        #return Render('_presentation.html',RequestContext(request, context))
        return HttpResponseRedirect(reverse('my-profile'))
    return HttpResponse(status=405)
