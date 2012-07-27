#coding=utf-8
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.template import loader
from django.conf import settings
import hashlib
import base64
import random
random.seed()
from localization.models import *
from profiles.models import *

#TODO: definir plantilla de correo
def send_confirmation_email(user):
    subject = "Confirma tu registro para el PyConVE-2012"
    from_email = settings.DEFAULT_FROM_EMAIL
    to = user.email
    html_content = loader.render_to_string('profiles/email_confirmation.html', {'site': settings.SITE_NAME, 'user': user})
    txt_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(subject, txt_content, from_email, [to])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def create_userprofile(user):
    profile = UserProfile(user=user)
    profile.save()
    return profile


def create_regprofile(user):
    user.is_active = False
    user.save()
    token = hashlib.md5(str(random.random())).hexdigest()
    encoded = base64.b64encode('%s|%s' % (user.email, token))
    reg = RegistrationProfile(user=user, token=token, encoded=encoded)
    reg.save()
    return reg
