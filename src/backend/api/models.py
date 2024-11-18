from django.db import models
from django.contrib.auth.models import User

class Server(models.Model):
    name = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()

class Invoice(models.Model):
    reference = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class Ticket(models.Model):
    subject = models.CharField(max_length=255)
    description = models.TextField()

class Notification(models.Model):
    message = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
