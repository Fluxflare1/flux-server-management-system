from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability_status = models.CharField(max_length=50, choices=[('available', 'Available'), ('unavailable', 'Unavailable')])
    created_at = models.DateTimeField(auto_now_add=True)
