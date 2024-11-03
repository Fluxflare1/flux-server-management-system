from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ActivityLog

class ActivityLogView(APIView):
    def get(self, request):
        logs = ActivityLog.objects.all()
        return Response(logs)
