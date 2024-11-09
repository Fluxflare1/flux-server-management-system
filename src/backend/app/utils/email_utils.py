# src/backend/app/utils/email_utils.py

from django.core.mail import send_mail
from django.conf import settings

def send_custom_email(subject, message, recipient_list, from_email=None):
    try:
        send_mail(
            subject,
            message,
            from_email or settings.DEFAULT_FROM_EMAIL,
            recipient_list,
            fail_silently=False,
        )
        return {"status": "success", "message": "Email sent successfully"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
