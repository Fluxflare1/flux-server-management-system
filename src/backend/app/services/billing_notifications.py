import smtplib
from email.mime.text import MIMEText
from config.logging_config import log_error

def send_billing_notification(user_email, usage_threshold):
    try:
        msg = MIMEText(f"Dear User, you have reached {usage_threshold}% of your usage limit.")
        msg["Subject"] = "Usage Alert"
        msg["From"] = "no-reply@fluxsystem.com"
        msg["To"] = user_email

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login("your_smtp_email", "your_smtp_password")
            server.sendmail("no-reply@fluxsystem.com", user_email, msg.as_string())
    except Exception as e:
        log_error(f"Failed to send billing notification: {e}")
