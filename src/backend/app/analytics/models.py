
from django.db import models

class AnalyticsRecord(models.Model):
    metric_name = models.CharField(max_length=255)
    value = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)



from django.db import models

class AnalyticsReport(models.Model):
    report_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()
