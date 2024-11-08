

# settings_dev.py
from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'mydb_dev',
    'USER': 'myuser',
    'PASSWORD': 'password',
    'HOST': 'localhost',
    'PORT': '5432',
}




# settings_dev.py
from .base import *

DEBUG = True
ALLOWED_HOSTS = []
