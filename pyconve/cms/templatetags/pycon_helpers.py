from django.template import Library
from django.contrib.auth.forms import AuthenticationForm
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
            'title': p.name,
            'speaker': speaker.get_full_name(),
            'about_speaker': UserProfile.objects.get(user=speaker).about,
            'avatar': avatar,
            'description': p.description,
            'tipo': tipo
        }
        p_data.append(data)

    return {'speakers':p_data}
