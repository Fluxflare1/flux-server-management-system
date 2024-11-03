from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    name = models.CharField(max_length=255)
    permissions = models.ManyToManyField('Permission')

class Permission(models.Model):
    code = models.CharField(max_length=255)
    description = models.TextField()
