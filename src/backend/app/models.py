from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    def has_permission(self, permission_name):
        return self.role.permissions.filter(name=permission_name).exists()

class Permission(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    roles = models.ManyToManyField(Role, related_name="permissions")

    def __str__(self):
        return self.name
