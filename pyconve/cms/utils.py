#coding=utf-8
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from cms.models import UserProfile, RegistrationProfile
import random
random.seed()
import hashlib
import base64

def registrationprofile_create(user):
    user.is_active = False
    user.save()
    token = hashlib.md5(str(random.random())).hexdigest()
    encoded = base64.b64encode('%s|%s' % (user.email, token))
    reg = RegistrationProfile(user=user, token=token, encoded=encoded)
    reg.save()
    return reg


def userprofile_create(user):
    profile = UserProfile(user=user)
    profile.save()
    return profile

#TODO: definir plantilla de correo
def registration_email_check(user):
    subject="Confirm Registration"
    from_email=settings.DEFAULT_FROM_EMAIL
    to=user.email
    html_content=loader.render_to_string('cms/email_confirmation.html',{'site':settings.SITE_NAME,'user':user})
    txt_content=strip_tags(html_content)
    msg=EmailMultiAlternatives(subject,txt_content,from_email,[to])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
