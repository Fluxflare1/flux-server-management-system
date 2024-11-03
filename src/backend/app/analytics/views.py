


from rest_framework import viewsets
from .models import AnalyticsRecord
from .serializers import AnalyticsRecordSerializer
from rest_framework.permissions import IsAuthenticated

class AnalyticsRecordViewSet(viewsets.ModelViewSet):
    queryset = AnalyticsRecord.objects.all()
    serializer_class = AnalyticsRecordSerializer
    permission_classes = [IsAuthenticated]




from rest_framework.views import APIView
from rest_framework.response import Response
from .analytics_manager import AnalyticsManager

class AnalyticsView(APIView):
    def get(self, request):
        manager = AnalyticsManager()
        report = manager.generate_report('usage')
        return Response(report)
