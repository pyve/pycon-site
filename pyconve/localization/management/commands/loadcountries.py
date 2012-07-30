#coding=utf-8
from django.core.management.base import BaseCommand,CommandError
from localization.models import Country
import csv
import os

class Command(BaseCommand):
    args=''
    help='Loads countries'

    def handle(self,*args,**kwargs):
        reader=csv.reader(open(os.path.join(os.path.dirname(__file__),'countries.csv'),'r'),delimiter=",",quotechar='"')
        for abb,name in reader:
            #name=name.decode('latin-1').encode('utf-8')
            c,created=Country.objects.get_or_create(name=name,abbreviation=abb)
            if created:
                self.stdout.write("Successfully created country: %s\n"%name)
            else:
                self.stdout.write("The country %s already existed\n"%name)
