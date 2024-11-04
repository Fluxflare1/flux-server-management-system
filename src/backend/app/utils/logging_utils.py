import logging

logger = logging.getLogger('myapp')

def log_action(action, user, details):
    logger.info(f"{action} by {user}: {details}")
