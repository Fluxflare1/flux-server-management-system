# src/backend/app/server_management/models.py
from django.db import models

class ServerInstance(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('running', 'Running'), ('stopped', 'Stopped')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
