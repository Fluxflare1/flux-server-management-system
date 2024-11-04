# In your models.py
class ActivityLog(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField()

    class Meta:
        indexes = [
            models.Index(fields=['timestamp']),
            models.Index(fields=['user_id', 'action_type']),
        ]
