#coding=utf-8
from django.core.management.base import BaseCommand,CommandError
from localization.models import Country,State
import csv
import os

class Command(BaseCommand):
    args=''
    help='Loads states'
    cache={}

    def handle(self,*args,**kwargs):
        reader=csv.reader(open(os.path.join(os.path.dirname(__file__),'states.csv'),'r'),delimiter=",",quotechar='"')
        for abb,name in reader:
#            name=name.decode('latin-1').encode('utf-8')
            if self.cache.has_key(abb):
                country=self.cache[abb]
            else:
                try:
                    country=Country.objects.get(abbreviation=abb)
                    self.cache[abb]=country
                except:
                    self.stdout.write("Couldnt load %s. There is no country with abbreviation %s\n"%(name,abb))
                    continue
            c,created=State.objects.get_or_create(name=name,country=country)
            if created:
                self.stdout.write("Successfully created state: %s\n"%name)
            else:
                self.stdout.write("State %s from %s already existed \n"%(name,country.name))
