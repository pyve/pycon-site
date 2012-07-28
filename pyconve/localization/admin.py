#coding=utf-8
from django.contrib import admin
from localization.models import *

class StateInline(admin.TabularInline):
    model=State
    extra=0

class CountryAdmin(admin.ModelAdmin):
    fields=('name',)
    inlines=(StateInline,)
admin.site.register(Country,CountryAdmin)
