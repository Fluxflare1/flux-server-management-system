# src/backend/logging/audit_logs.py

from datetime import datetime
from src.backend.database import save_audit_log  # Assuming a logging function

def log_audit_event(user_id, action, details):
    """
    Logs important administrative actions for auditing purposes.
    """
    audit_entry = {
        "user_id": user_id,
        "action": action,
        "details": details,
        "timestamp": datetime.utcnow()
    }
    save_audit_log(audit_entry)
