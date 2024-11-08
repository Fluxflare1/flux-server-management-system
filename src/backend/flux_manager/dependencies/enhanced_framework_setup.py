# src/backend/flux_manager/dependencies/enhanced_framework_setup.py

import subprocess

def setup_framework_environment(framework, config):
    if framework == 'Django':
        setup_django_environment(config)
    elif framework == 'Flask':
        setup_flask_environment(config)

def setup_django_environment(config):
    subprocess.run(["pip", "install", "django", "djangorestframework", "channels"])
    subprocess.run(["django-admin", "startproject", config['project_name']])
    configure_django_channels(config['project_name'])

def setup_flask_environment(config):
    subprocess.run(["pip", "install", "flask", "flask-restful", "flask-socketio"])
    create_flask_structure(config['project_name'])
