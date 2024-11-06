# src/backend/jobs/audit_report_scheduler.py

import time
from src.backend.reporting.audit_report_generator import generate_audit_report
from src.backend.monitoring.email_service import send_report_email  # Assuming email service

def schedule_audit_reports():
    """
    Generates and sends audit reports on a scheduled basis.
    """
    while True:
        report = generate_audit_report()
        send_report_email("admin@example.com", "Weekly Audit Report", report)
        time.sleep(604800)  # Send weekly
