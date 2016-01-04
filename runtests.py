#!/usr/bin/env python

from __future__ import unicode_literals

import django

from django.conf import settings, global_settings
from django.core.management import call_command

settings.configure(
    MIDDLEWARE_CLASSES=global_settings.MIDDLEWARE_CLASSES,
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sites',
        'django.contrib.admin',
        'django.contrib.sessions',
        'automatic_links',
    ),
    DATABASES={
        'default': {'ENGINE': 'django.db.backends.sqlite3'}
    }
)

from django.test.utils import setup_test_environment
setup_test_environment()

if django.VERSION > (1, 7):
    django.setup()

if __name__ == '__main__':
    call_command('test', 'automatic_links')
