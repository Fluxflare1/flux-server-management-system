# src/backend/routes/report_settings.py

from flask import Blueprint, jsonify
from src.backend.middleware.rbac_middleware import authorize

report_settings_bp = Blueprint('report_settings', __name__)

@report_settings_bp.route('/schedule_report', methods=['POST'])
@authorize('schedule', 'analytics_reports')
def schedule_report():
    # Logic for scheduling a report
    return jsonify({"message": "Report scheduled successfully"}), 200

@report_settings_bp.route('/settings', methods=['POST'])
@authorize('edit', 'report_settings')
def edit_report_settings():
    # Logic for updating report settings
    return jsonify({"message": "Report settings updated"}), 200
