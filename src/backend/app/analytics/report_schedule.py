# src/backend/app/analytics/report_schedule.py

import schedule
from report_generation import generate_report

def schedule_reports():
    schedule.every().month.do(generate_report)
