# src/backend/app/views/resource_monitoring.py
import psutil
from rest_framework.views import APIView
from rest_framework.response import Response

class ResourceMonitoringView(APIView):
    def get(self, request):
        """Get server resource usage metrics."""
        metrics = {
            "cpu": psutil.cpu_percent(interval=1),
            "memory": psutil.virtual_memory().percent,
            "disk": psutil.disk_usage('/').percent,
        }
        return Response(metrics)
