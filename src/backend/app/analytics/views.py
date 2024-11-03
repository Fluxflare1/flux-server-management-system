from rest_framework.views import APIView
from rest_framework.response import Response
from .analytics_manager import AnalyticsManager

class AnalyticsView(APIView):
    def get(self, request):
        manager = AnalyticsManager()
        report = manager.generate_report('usage')
        return Response(report)
