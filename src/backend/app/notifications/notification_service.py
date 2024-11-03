from django.core.mail import send_mail

class NotificationService:
    def send_email(self, subject, message, recipient_list):
        send_mail(subject, message, 'no-reply@example.com', recipient_list)
