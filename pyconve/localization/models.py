from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=64)
    abbreviation = models.CharField(max_length=2, default='OT')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s'%self.name

class State(models.Model):
    name = models.CharField(max_length=64)
    country = models.ForeignKey(Country)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s'%self.name

