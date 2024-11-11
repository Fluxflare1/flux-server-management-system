from app.notifications import send_email_notification

def check_user_balance(user):
    if user.balance < 10:  # Example threshold
        subject = "Low Balance Alert"
        body = "Your balance is low. Please top up to avoid service interruption."
        send_email_notification(user.email, subject, body)
