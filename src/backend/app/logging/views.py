from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AuditLog
from .audit_logger import log_action

class AuditLogView(APIView):
    def get(self, request):
        logs = AuditLog.objects.all()
        # Format and return logs
        return Response(logs)
