# src/backend/auth/contextual_permissions.py

from datetime import datetime

def check_contextual_permissions(user, action):
    """
    Checks if a user's permissions are valid within the current context.
    """
    current_hour = datetime.now().hour
    if user.role == "restricted_user" and current_hour < 8:
        return False  # Restrict actions outside business hours
    return True
