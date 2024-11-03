from django.db import models

class AuditLog(models.Model):
    user = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
