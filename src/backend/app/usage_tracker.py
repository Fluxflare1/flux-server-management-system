def update_user_balance(user, usage):
    cost = usage * 0.10  # Example cost per unit of usage
    user.balance -= cost
    user.save()
