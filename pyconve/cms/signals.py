#coding=utf-8
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from cms.utils import userprofile_create as up_create, registrationprofile_create as rp_create, registration_email_check as email_check

def signal_new_user(sender, instance, created, *args, **kwargs):
    user = instance
    if created:
        up_create(user)
        if instance.email:
            rp_create(user)
            email_check(user)
post_save.connect(signal_new_user, sender=User)
