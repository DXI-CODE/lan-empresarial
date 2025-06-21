from .common import *

SECRET_KEY = 'your-random-secret-key-5x893254x89532478'
DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'taiga',
        'USER': 'taiga',
        'PASSWORD': 'taiga123',
        'HOST': 'taiga_db',
        'PORT': '5432',
    }
}
