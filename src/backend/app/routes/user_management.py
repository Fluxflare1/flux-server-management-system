# src/backend/routes/user_management.py

from flask import Blueprint, jsonify
from src.backend.middleware.rbac_middleware import authorize

user_mgmt_bp = Blueprint('user_mgmt', __name__)

@user_mgmt_bp.route('/users', methods=['GET'])
@authorize('view', 'user_management')
def get_users():
    # Logic to retrieve and return user data
    return jsonify({"users": []}), 200

@user_mgmt_bp.route('/users/<int:user_id>', methods=['DELETE'])
@authorize('delete', 'user_management')
def delete_user(user_id):
    # Logic to delete a user
    return jsonify({"message": f"User {user_id} deleted"}), 200
