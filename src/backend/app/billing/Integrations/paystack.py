import requests
from django.conf import settings

class PaystackIntegration:
    @staticmethod
    def initiate_payment(amount, user_email):
        url = "https://api.paystack.co/transaction/initialize"
        headers = {
            "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "email": user_email,
            "amount": amount * 100  # Amount in kobo
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()
