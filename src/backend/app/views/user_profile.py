# src/backend/app/views/user_profile.py
from flask import Blueprint, request, jsonify
from models import User
from utils.auth import login_required

user_profile_bp = Blueprint('user_profile', __name__)

@user_profile_bp.route('/profile', methods=['GET'])
@login_required
def get_profile():
    user = User.get_by_id(request.user.id)
    return jsonify(user.serialize())

@user_profile_bp.route('/profile', methods=['PUT'])
@login_required
def update_profile():
    data = request.json
    user = User.update(request.user.id, **data)
    return jsonify(user.serialize())
