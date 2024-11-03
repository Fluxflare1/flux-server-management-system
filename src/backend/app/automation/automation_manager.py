import schedule
import time

class AutomationManager:
    def perform_daily_health_check(self):
        # Logic to perform health check
        pass

    def setup_scheduled_tasks(self):
        schedule.every().day.at("02:00").do(self.perform_daily_health_check)

    def run_pending_tasks(self):
        while True:
            schedule.run_pending()
            time.sleep(1)
