#!/usr/bin/env python
import sys
import os
import time
from optparse import OptionParser
import fapws._evwsgi as evwsgi
from fapws import base
from fapws.contrib import django_handler, views
import django

parser = OptionParser()
parser.set_defaults(
    port='8000',
    host='127.0.0.1',
    settings='settings',
)

parser.add_option('--port', dest='port')
parser.add_option('--host', dest='host')
parser.add_option('--settings', dest='settings')
parser.add_option('--pythonpath', dest='pythonpath')

options, args = parser.parse_args()
os.environ['DJANGO_SETTINGS_MODULE'] = options.settings

sys.setcheckinterval=100000 # since we don't use threads, internal checks are no more required

if options.pythonpath:
    sys.path.insert(0, options.pythonpath)

print 'start on', (options.host, options.port)
evwsgi.start(options.host, options.port)
evwsgi.set_base_module(base)

def generic(environ, start_response):
    res=django_handler.handler(environ, start_response)
    return [res]

evwsgi.wsgi_cb(('',generic))
evwsgi.set_debug(True)
evwsgi.run()
