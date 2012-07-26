#coding=utf-8
from django.db.models.signals import post_save
from django.contrib.auth.models import User
import profiles.utils as utils

def new_user_signal(sender, instance, created, *args, **kwargs):
    user = instance
    if created:
        utils.create_userprofile(user)
        if user.email:
            utils.create_regprofile(user)
            utils.self_confirmation_email(user)
post_save.connect(new_user_signal, sender=User)
