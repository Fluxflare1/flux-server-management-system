# src/backend/auth/custom_roles.py

from src.backend.database import db_session
from src.backend.models import CustomRole

def create_custom_role(name, permissions):
    """
    Create a new custom role with specified permissions.
    """
    new_role = CustomRole(name=name, permissions=permissions)
    db_session.add(new_role)
    db_session.commit()
    return new_role

def update_custom_role(role_id, permissions):
    """
    Update an existing custom role with new permissions.
    """
    role = db_session.query(CustomRole).get(role_id)
    if role:
        role.permissions = permissions
        db_session.commit()
        return role
    return None

def delete_custom_role(role_id):
    """
    Delete a custom role.
    """
    role = db_session.query(CustomRole).get(role_id)
    if role:
        db_session.delete(role)
        db_session.commit()
        return True
    return False
