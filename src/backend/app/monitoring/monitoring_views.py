import psutil
from django.http import JsonResponse

def system_metrics(request):
    metrics = {
        'cpu_usage': psutil.cpu_percent(),
        'memory_usage': psutil.virtual_memory().percent,
        'disk_usage': psutil.disk_usage('/').percent,
    }
    return JsonResponse(metrics)
