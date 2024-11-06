# src/backend/auth/role_hierarchy.py

def get_permissions_for_role(role):
    """
    Retrieves permissions for a role, including inherited permissions.
    """
    base_permissions = role.permissions
    if role.parent_role:
        base_permissions.update(role.parent_role.permissions)
    return base_permissions
