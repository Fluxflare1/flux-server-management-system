# src/backend/app/payment/invoice.py

from payment_gateway import PaymentGatewayClient

def generate_invoice(user_id, amount):
    # Logic to generate invoice based on user and usage data
    pass

def process_payment(invoice_id, payment_data):
    payment_client = PaymentGatewayClient()
    response = payment_client.process_payment(invoice_id, payment_data)
    return response
