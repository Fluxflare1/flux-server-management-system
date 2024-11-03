

from rest_framework import viewsets
from .models import Invoice, Payment, UsageRecord
from .serializers import InvoiceSerializer, PaymentSerializer, UsageRecordSerializer
from rest_framework.permissions import IsAuthenticated

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

class UsageRecordViewSet(viewsets.ModelViewSet):
    queryset = UsageRecord.objects.all()
    serializer_class = UsageRecordSerializer
    permission_classes = [IsAuthenticated]




from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BillingRecord
from .billing_manager import BillingManager

class BillingView(APIView):
    def get(self, request):
        user_id = request.user.id
        manager = BillingManager()
        usage = manager.calculate_usage(user_id)
        return Response({"usage": usage})
