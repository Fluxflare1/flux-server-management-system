from django.http import JsonResponse
from .models import Notification

def notifications_view(request):
    notifications = Notification.objects.order_by('-timestamp')[:50]
    data = [
        {"id": n.id, "message": n.message, "timestamp": n.timestamp}
        for n in notifications
    ]
    return JsonResponse(data, safe=False)
