# src/backend/auth/mfa.py

from some_mfa_library import initiate_mfa

def enforce_mfa(user):
    """
    Enforces MFA based on user's role.
    """
    if user.role in ["admin", "super_admin"]:
        return initiate_mfa(user)
    return True
