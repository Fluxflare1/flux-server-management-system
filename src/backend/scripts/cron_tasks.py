import schedule
import time
from app.billing import check_user_balance
from app.auto_suspend import auto_suspend_user_instance

def run_balance_checks():
    # Logic to loop through all users and check balance
    for user in get_all_users():
        check_user_balance(user)
        if user.balance <= 0:
            auto_suspend_user_instance(user)

# Schedule tasks
schedule.every(30).minutes.do(run_balance_checks)

while True:
    schedule.run_pending()
    time.sleep(1)
