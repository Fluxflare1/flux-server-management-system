from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    subscription_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
