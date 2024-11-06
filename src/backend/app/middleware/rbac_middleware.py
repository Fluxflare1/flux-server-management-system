# src/backend/middleware/rbac_middleware.py

from functools import wraps
from flask import request, jsonify, session
from src.backend.auth.roles import ROLES

def authorize(action, resource):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user_role = session.get('role')  # Assume role is stored in session after login
            if not user_role:
                return jsonify({"error": "Unauthorized"}), 401
            permissions = ROLES.get(user_role, {})
            if resource in permissions.get(action, []):
                return f(*args, **kwargs)
            return jsonify({"error": "Permission denied"}), 403
        return decorated_function
    return wrapper
