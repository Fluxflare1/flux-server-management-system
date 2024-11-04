# src/backend/app/views/monitoring.py
import psutil
from flask import jsonify, Blueprint

monitoring_bp = Blueprint('monitoring', __name__)

@monitoring_bp.route('/metrics', methods=['GET'])
def get_metrics():
    metrics = {
        'cpu': psutil.cpu_percent(),
        'memory': psutil.virtual_memory().percent,
        'storage': psutil.disk_usage('/').percent
    }
    return jsonify(metrics)
