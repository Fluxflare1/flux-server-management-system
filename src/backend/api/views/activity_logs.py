from django.http import JsonResponse
from .models import ActivityLog

def activity_logs_view(request):
    logs = ActivityLog.objects.order_by('-timestamp')[:100]
    data = [
        {"id": log.id, "user": log.user.username, "action": log.action, "timestamp": log.timestamp}
        for log in logs
    ]
    return JsonResponse(data, safe=False)
