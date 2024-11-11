from flask import Blueprint, request, jsonify
from .utils import provision_server

provision_bp = Blueprint('provision', __name__)

@provision_bp.route('/api/provision', methods=['POST'])
def provision():
    data = request.json
    hosting_type = data.get("hosting_type")  # "Dedicated", "VPS", or "Shared"
    resources = data.get("resources")  # {"cpu": 2, "ram": 4096, "storage": 50}

    server_details = provision_server(hosting_type, resources)
    return jsonify(server_details), 201
