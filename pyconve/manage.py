#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyconve.settings")

    from django.core.management import execute_from_command_line

    if sys.argv[1] == 'syncdb':
        print "If you're prompted to create an admin user, PLEASE say no"
        print "an admin user will be created when you migrate the profiles app"

    execute_from_command_line(sys.argv)

    if sys.argv[1] == 'migrate' and sys.argv[2] == 'profiles':
        from django.contrib.auth.models import User
        if User.objects.count() == 0:
            User.objects.create_superuser('admin', 'admin@admin.com', '1qaz')
            print "Admin user created as:"
            print "User: admin"
            print "pass: 1qaz"

    if sys.argv[1] == 'migrate' and sys.argv[2] == 'localization':
        from localization.models import *
        if Country.objects.count() == 0:
            execute_from_command_line(['manage.py', 'loadcountries'])
            execute_from_command_line(['manage.py', 'loadstates'])
