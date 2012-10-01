#coding=utf-8
from __future__ import unicode_literals
from django.template import Library
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.template.defaultfilters import truncatewords
from profiles.models import Sponsor, UserProfile
from cms.models import Presentation
import hashlib
import urllib

register = Library()

@register.inclusion_tag('_sponsors.html')
def show_sponsors():
    return {'sponsors':Sponsor.objects.all()}

@register.inclusion_tag('_chats.html')
def show_speakers():
    chats = Presentation.objects.filter(approved=True)
    p_data = []

    for p in chats:
        url = 'http://www.gravatar.com/avatar/%s'
        speaker = p.speakers.all()[0]
        email = speaker.email
        avatar = url % hashlib.md5(email).hexdigest()
        tipo = 'Charla'
        if p.tutorial:
            tipo = 'Tutorial'
        data = {
            'detail': reverse('presentation-view', kwargs={'presentation_id': p.id}),
            'title': p.name,
            'speaker': speaker.get_full_name(),
            'avatar': avatar,
            'description': truncatewords(p.description, 25),
        }
        p_data.append(data)

    return {'speakers':p_data}
