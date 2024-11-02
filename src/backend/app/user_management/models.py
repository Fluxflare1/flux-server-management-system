# src/backend/app/user_management/models.py
from django.contrib.auth.models import AbstractUser, Group
from django.db import models

class User(AbstractUser):
    role = models.CharField(max_length=50)
