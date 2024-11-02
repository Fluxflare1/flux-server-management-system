# src/backend/app/resource_monitoring/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import psutil

class MetricsView(APIView):
    def get(self, request):
        # Collect system metrics
        metrics = {
            "cpu": psutil.cpu_percent(interval=1),
            "memory": psutil.virtual_memory().percent,
            "disk": psutil.disk_usage('/').percent,
        }
        return Response(metrics, status=status.HTTP_200_OK)
