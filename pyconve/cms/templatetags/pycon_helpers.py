from django.template import Library
from django.contrib.auth.forms import AuthenticationForm
from profiles.models import Sponsor
from cms.models import Presentation
import hashlib
import urllib

register = Library()

@register.inclusion_tag('_sponsors.html')
def show_sponsors():
    return {'sponsors':Sponsor.objects.all()}

@register.inclusion_tag('_chats.html')
def show_speakers():
    chats = Presentation.objects.all()
    p_data = []

    for p in chats:
        import pdb;pdb.set_trace()
        url = 'http://www.gravatar.com/avatar/%s'
        speaker = p.speakers[0]
        email = speaker.email
        name = p.speaker.get_full_name()
        avatar = url % hashlib.md5(email).hexdigest()
        data = {
            'title': p.name,
            'speaker': name,
            'avatar': avatar,
        }
        p_data.append(data)

    return {'speakers':p_data}
