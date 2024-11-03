from rest_framework.views import APIView
from rest_framework.response import Response
from .backup_manager import BackupManager

class BackupView(APIView):
    def post(self, request):
        manager = BackupManager()
        manager.create_backup()
        return Response({"status": "backup created"})
