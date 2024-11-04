# src/backend/app/payments/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .paystack_service import initialize_transaction, verify_transaction

class InitializePaymentView(APIView):
    def post(self, request):
        email = request.data.get("email")
        amount = request.data.get("amount")
        response = initialize_transaction(email, amount)
        return Response(response, status=status.HTTP_200_OK)

class VerifyPaymentView(APIView):
    def get(self, request, reference):
        response = verify_transaction(reference)
        return Response(response, status=status.HTTP_200_OK)
