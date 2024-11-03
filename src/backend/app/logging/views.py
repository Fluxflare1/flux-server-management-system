

from rest_framework import viewsets
from .models import ActivityLog
from .serializers import ActivityLogSerializer
from rest_framework.permissions import IsAuthenticated

class ActivityLogViewSet(viewsets.ModelViewSet):
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer
    permission_classes = [IsAuthenticated]




from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AuditLog
from .audit_logger import log_action

class AuditLogView(APIView):
    def get(self, request):
        logs = AuditLog.objects.all()
        # Format and return logs
        return Response(logs)
