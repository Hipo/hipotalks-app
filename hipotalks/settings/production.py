from os.path import dirname, abspath

from .base import *
from .secrets_production import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'hipotalks_production',
        'USER': 'hipotalks_dbu',
        'PASSWORD': 'wlkrtjesrlkna',
        'HOST': 'hipotalks_postgres',
        'PORT': '5432',
    }
}


BASE_URL = ''


MEDIA_ROOT = os.path.join(dirname(dirname(dirname(abspath(__file__)))), 'media/files/')
STATIC_ROOT = os.path.join(dirname(dirname(dirname(abspath(__file__)))), 'static/')

STATICFILES_DIRS = (
    ('', abspath(os.path.join(dirname(dirname(dirname(abspath(__file__)))), 'frontend/'))),
)

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'