

# settings_prod.py
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['your-domain.com']
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'mydb_prod',
    'USER': 'myuser',
    'PASSWORD': 'secure_password',
    'HOST': 'your-database-host.com',
    'PORT': '5432',
}
