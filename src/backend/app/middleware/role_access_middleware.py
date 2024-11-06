# src/backend/middleware/role_access_middleware.py

from flask import request, g
from functools import wraps
from src.backend.auth.roles import has_permission
from src.backend.middleware.access_logging import log_access

def authorize_with_logging(action, resource):
    def wrapper(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            user_id = g.user_id  # Assuming user ID is stored in request context
            role = g.role        # Assuming role is stored in request context
            if has_permission(role, action, resource):
                log_access(user_id, role, action, "success", resource)
                return func(*args, **kwargs)
            else:
                log_access(user_id, role, action, "failure", resource)
                return {"error": "Access Denied"}, 403
        return decorated_function
    return wrapper
