# src/backend/flux_manager/dependencies/framework_setup.py

def setup_django_project(config):
    import subprocess
    # Install Django and dependencies
    subprocess.run(["pip", "install", "django"])
    # Initialize Django project
    subprocess.run(["django-admin", "startproject", config['project_name']])

def setup_flask_project(config):
    import subprocess
    # Install Flask and dependencies
    subprocess.run(["pip", "install", "flask"])
    # Initialize Flask project structure
    create_flask_structure(config['project_name'])
