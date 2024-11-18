from django.http import JsonResponse
import psutil

def system_health_view(request):
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    storage = psutil.disk_usage('/')
    
    data = {
        "cpu": [cpu_usage],
        "memory": [memory.percent],
        "storage": [storage.percent],
    }
    return JsonResponse(data)
