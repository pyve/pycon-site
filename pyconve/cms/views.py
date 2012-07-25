#coding=utf-8
from django.shortcuts import render_to_response as Render, get_object_or_404 as get404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import simplejson
from cms.models import *
from cms.forms import *

def home(request):
	context = {}
	return Render('base.html', RequestContext(request, context))


def presentation_create(request):
    """
    GET: shows the presentation registration form
    POST: saves all the information
    """
    context = {}
    if request.method == 'POST':
        form = PresentationForm(request.POST)
        if form.is_valid():
            p = Presentation()
            p.speakers = form.cleaned_data['speakers']
            p.name = form.cleaned_data['name']
            p.description = form.cleaned_nada['description']
            p.tutorial = form.cleaned_data['tutorial']
            p.duration = form.cleaned_data['duration']
            p.requirements = form.cleaned_data['requirements']
            p.save()
            context = {'status_message': 'Charla creada'}
            return HttpResponse(simplejson.dumps(context))
        else:
            context = {'status_message': form.errors}
            return simplejson.dumps(context)
    else:
        context = {'form': PresentationForm()}
    return Render('cms/presentation_create.html', RequestContext(request, context))


def presentation_list(request):
    presentations = Presentation.objects.all()
    context = {'data': presentations}
    return Render('cms/presentation_list.html', RequestContext(request, context))


def presentation_view(request, presentation_id):
    p = get404(Presentation, id=presentation_id)
    context = {'data': p}
    return Render('cms/presentation_view.html', RequestContext(request, context))


def presentation_edit(request, presentation_id):
    """
    GET: show the presentation edit form
    POST: validates and saves all the information
    """
    context = {}
    p = get404(Presentation, id=presentation_id)
    if request.method == 'POST':
        if form.is_valid():
            if request.user in p.speakers.all():
                p.speakers = form.cleaned_data['speakers']
                p.name = form.cleaned_data['name']
                p.description = form.cleaned_nada['description']
                p.tutorial = form.cleaned_data['tutorial']
                p.duration = form.cleaned_data['duration']
                p.requirements = form.cleaned_data['requirements']
                p.save()
                context = {'status_message': 'Cambios realizados'}
                return HttpResponse(simplejson.dumps(context))
            else:
                context = {'status_message': 'Debes ser uno de los ponentes para editar la charla'}
                return HttpResponse(status=403, content=context)
        else:
            context = {'status_message': form.errors}
            return HttpResponse(status=400, content=simplejson.dumps(context))
    else:
        data = {
            'speakers': p.speakers.all(),
            'name': p.name,
            'description': p.description(),
            'tutorial': p.tutorial,
            'duration': p.duration,
            'requirements': p.requirements,
        }
        context = {'data', data}
    return Render('cms/presentation_edit.html', RequestContext(request, context))


