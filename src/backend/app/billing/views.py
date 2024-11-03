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
