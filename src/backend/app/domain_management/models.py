from django.db import models

class Domain(models.Model):
    client = models.ForeignKey('client_management.Client', on_delete=models.CASCADE)
    domain_name = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('expired', 'Expired')])
    renewal_date = models.DateField()
