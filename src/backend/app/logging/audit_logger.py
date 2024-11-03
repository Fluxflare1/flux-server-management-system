import logging

# Setting up audit logger
audit_logger = logging.getLogger("audit")
handler = logging.FileHandler("audit.log")
formatter = logging.Formatter('%(asctime)s - %(user)s - %(action)s - %(status)s')
handler.setFormatter(formatter)
audit_logger.addHandler(handler)
audit_logger.setLevel(logging.INFO)

def log_action(user, action, status="success"):
    audit_logger.info('', extra={'user': user, 'action': action, 'status': status})
