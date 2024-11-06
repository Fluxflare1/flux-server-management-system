# src/backend/monitoring/alerts.py

import logging
from datetime import datetime, timedelta
from src.backend.database import get_failed_access_attempts  # Utility to fetch failed attempts
from src.backend.monitoring.email_service import send_alert_email  # Assume email service for alerts

logger = logging.getLogger(__name__)

def monitor_failed_attempts():
    """
    Checks recent failed access attempts and sends an alert if necessary.
    """
    alert_threshold = 5  # Example threshold
    time_window = datetime.utcnow() - timedelta(minutes=15)
    
    failed_attempts = get_failed_access_attempts(since=time_window)
    
    if len(failed_attempts) > alert_threshold:
        send_alert_email("admin@example.com", "Suspicious Activity Alert",
                         f"{len(failed_attempts)} failed access attempts detected.")
        logger.warning("Suspicious activity detected and alert sent to admin.")
