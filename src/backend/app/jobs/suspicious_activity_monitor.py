# src/backend/jobs/suspicious_activity_monitor.py

import time
from src.backend.monitoring.alerts import monitor_failed_attempts

def start_suspicious_activity_monitor():
    while True:
        monitor_failed_attempts()
        time.sleep(900)  # Run every 15 minutes
