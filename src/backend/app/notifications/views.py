from rest_framework.views import APIView
from rest_framework.response import Response
from .notification_service import NotificationService

class NotificationView(APIView):
    def post(self, request):
        service = NotificationService()
        service.send_email("Alert", "This is a notification", [request.user.email])
        return Response({"status": "notification sent"})
