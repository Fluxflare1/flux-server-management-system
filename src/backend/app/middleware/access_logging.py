# src/backend/middleware/access_logging.py

import logging
from datetime import datetime
from src.backend.database import save_log  # Assuming a logging utility

logger = logging.getLogger(__name__)

def log_access(user_id, role, action, status, resource):
    """
    Logs access attempts and role-based actions.
    """
    timestamp = datetime.utcnow()
    log_entry = {
        "user_id": user_id,
        "role": role,
        "action": action,
        "status": status,  # 'success' or 'failure'
        "resource": resource,
        "timestamp": timestamp
    }
    save_log(log_entry)
    logger.info(f"User {user_id} with role {role} attempted {action} on {resource} - {status}")
