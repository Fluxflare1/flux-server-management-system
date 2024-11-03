from django.db import models

class NotificationPreference(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    email_notifications = models.BooleanField(default=True)
    sms_notifications = models.BooleanField(default=False)
