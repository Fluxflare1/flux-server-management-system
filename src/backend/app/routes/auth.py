# src/backend/routes/auth.py

from flask import Blueprint, request, jsonify, session
from src.backend.auth.two_factor import TwoFactorAuth

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    # Perform initial user authentication
    user_id = authenticate_user(request.json.get('username'), request.json.get('password'))
    if user_id:
        # Generate and send 2FA code
        email = get_user_email(user_id)  # Fetch user email from database
        TwoFactorAuth.send_code(user_id, email)
        session['user_id'] = user_id
        return jsonify({"message": "2FA code sent to your email"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

@auth_bp.route('/verify-2fa', methods=['POST'])
def verify_2fa():
    user_id = session.get('user_id')
    code = request.json.get('code')
    if user_id and TwoFactorAuth.validate_code(user_id, int(code)):
        session['authenticated'] = True
        return jsonify({"message": "2FA verification successful"}), 200
    else:
        return jsonify({"error": "Invalid or expired code"}), 401
