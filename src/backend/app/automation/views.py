
from rest_framework.views import APIView
from rest_framework.response import Response
from .automation_service import AutomationService

class AutomationTasksView(APIView):
    def post(self, request):
        service = AutomationService()
        service.setup_automated_tasks()
        return Response({"status": "automated tasks set up"})




from rest_framework.views import APIView
from rest_framework.response import Response
from .automation_manager import AutomationManager

class AutomationView(APIView):
    def post(self, request):
        manager = AutomationManager()
        manager.setup_scheduled_tasks()
        return Response({"status": "scheduled tasks set up"})
