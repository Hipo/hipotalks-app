import redis
from .base import *
from .secrets_development import *

ALLOWED_HOSTS += [
    '.ngrok.io',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'hipotalks',
        'USER': 'hipotalks_dbu',
        'PASSWORD': 'test',
        'HOST': 'hipotalks_postgres',
        'PORT': '5432',
    }
}


REDIS_HOST = 'redis'
REDIS_PORT = 6379
REDIS_CELERY_NUMBER = 1
REDIS_CONNECTION = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=3, health_check_interval=20)

BASE_URL = 'http://localhost:8000'
