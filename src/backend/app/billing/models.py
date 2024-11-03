

from django.db import models

class UsageRecord(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    server_id = models.CharField(max_length=255)
    cpu_usage = models.FloatField()
    memory_usage = models.FloatField()
    storage_usage = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)

class Invoice(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()

class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')




from django.db import models

class BillingRecord(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    usage = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_date = models.DateField(auto_now_add=True)
