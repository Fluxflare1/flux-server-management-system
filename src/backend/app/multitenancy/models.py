from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=255)
    admin_user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    database_name = models.CharField(max_length=255)
