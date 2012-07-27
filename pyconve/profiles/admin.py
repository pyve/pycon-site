#coding=utf-8
from django.contrib import admin
from profiles.models import Sponsor

class SponsorAdmin(admin.ModelAdmin):
    fields = ('name', 'logo', 'website', 'sponsorship_type', 'description')

admin.site.register(Sponsor, SponsorAdmin)
