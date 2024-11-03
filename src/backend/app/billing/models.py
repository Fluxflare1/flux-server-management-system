from django.db import models

class BillingRecord(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    usage = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_date = models.DateField(auto_now_add=True)
