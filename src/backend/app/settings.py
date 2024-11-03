



# JWT settings
SECRET_KEY = 'your-secret-key'  # Replace with a secure key in production



import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': '5432',
    }
}

# Allow all hosts for testing; update for production use
ALLOWED_HOSTS = ["*"]
