# django_setup.py
import os
import subprocess

def setup_django_project(project_name):
    # Create Django project and app
    subprocess.run(f'django-admin startproject {project_name}', shell=True)
    subprocess.run(f'cd {project_name} && python manage.py startapp main', shell=True)
    
    # Initial migrations
    subprocess.run(f'cd {project_name} && python manage.py migrate', shell=True)

    print(f'{project_name} setup with initial migrations completed.')

if __name__ == '__main__':
    setup_django_project("my_project")
