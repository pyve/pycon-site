from django.db import models



class Country(models.Model):
    name = models.CharField(max_length=64)


class State(models.Model):
    name = models.CharField(max_length=64)
    country = models.ForeignKey(Country)
