import smtplib
from email.message import EmailMessage

def send_email_notification(user_email, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = "admin@yourdomain.com"
    msg['To'] = user_email

    # Replace with your SMTP server credentials
    with smtplib.SMTP('smtp.yourdomain.com', 587) as server:
        server.starttls()
        server.login("username", "password")
        server.send_message(msg)
