
from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=255)
    admin_user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class TenantResource(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    resource_name = models.CharField(max_length=255)
    resource_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)



from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=255)
    admin_user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    database_name = models.CharField(max_length=255)
