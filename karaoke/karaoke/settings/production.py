"""Production settings and globals."""

from os import environ

from base import *

import dj_database_url

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)

ALLOWED_HOSTS = [".herokuapp.com"]

########## DATABASE CONFIGURATION
DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost')
}
########## END DATABASE CONFIGURATION

# heroku static

import os
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(DJANGO_ROOT, 'karaoke/static'),
)
