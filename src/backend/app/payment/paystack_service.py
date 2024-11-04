# src/backend/app/payments/paystack_service.py

from paystackapi.transaction import Transaction
from django.conf import settings

Transaction.api_key = settings.PAYSTACK_SECRET_KEY

def initialize_transaction(email, amount):
    response = Transaction.initialize(
        reference="unique_transaction_reference",
        amount=int(amount * 100),  # amount in kobo
        email=email,
        currency="NGN",
    )
    return response

def verify_transaction(reference):
    response = Transaction.verify(reference)
    return response
