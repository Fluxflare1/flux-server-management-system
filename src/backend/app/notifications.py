from .models import Reseller
from django.core.mail import send_mail

def notify_reseller_commission_paid(reseller, commission):
    subject = "Your commission has been processed"
    message = f"Dear {reseller.name},\n\nYour commission of {commission.amount} has been successfully processed."
    send_mail(subject, message, 'support@yourplatform.com', [reseller.email])
