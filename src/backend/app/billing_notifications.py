import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_billing_notification(user_email, billing_info):
    """Sends a billing notification email to the user."""
    sender_email = "no-reply@fluxserver.com"
    receiver_email = user_email
    password = "your_email_password"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "Flux Server Billing Notification"

    body = f"Dear user,\n\nYour usage has reached the following billing status:\n{billing_info}\n\nBest regards,\nFlux Server Management Team"
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        return "Notification sent successfully"
    except Exception as e:
        return f"Failed to send notification: {str(e)}"
