from django.shortcuts import render_to_response as Render
from django.template import RequestContext

def home(request):
	context = {}
	return Render('base.html', RequestContext(request, context))