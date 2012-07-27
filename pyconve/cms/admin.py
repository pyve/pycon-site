#coding=utf-8
from django.contrib import admin
from cms.models import Presentation

class PresentationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Uso del administrador', {'fields': ['approved',]}),
        ('Datos de la charla', {'fields': ['name', 'tutorial', 'description', 'duration', 'requirements']})
    ]

admin.site.register(Presentation, PresentationAdmin)
