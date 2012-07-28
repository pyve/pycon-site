#coding=utf-8
from django.contrib import admin
from profiles.models import *

class SponsorAdmin(admin.ModelAdmin):
    fields = ('name', 'logo', 'website', 'sponsorship_type', 'description')
    list_filter=('sponsorship_type',)
admin.site.register(Sponsor, SponsorAdmin)

admin.site.register(RegistrationProfile)
admin.site.register(UserProfile)
