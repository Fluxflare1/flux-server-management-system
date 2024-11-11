def auto_suspend_user_instance(user):
    if user.balance <= 0:
        # Suspend logic
        user.is_suspended = True
        user.save()
