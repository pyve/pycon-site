from django.template import Library
from django.contrib.auth.forms import AuthenticationForm
from profiles.models import Sponsor

register = Library()

@register.inclusion_tag('_sponsors.html')
def show_sponsors():
    return {'sponsors':Sponsor.objects.all()}
