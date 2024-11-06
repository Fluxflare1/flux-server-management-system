# src/backend/auth/role_automation.py

def assign_role_based_on_activity(user, activity_score):
    """
    Assigns roles to users based on their activity score.
    """
    if activity_score > 100:
        user.role = "premium_user"
    elif activity_score > 50:
        user.role = "active_user"
    else:
        user.role = "new_user"
    db_session.commit()
