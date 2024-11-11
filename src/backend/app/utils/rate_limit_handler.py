import time
from config.logging_config import log_error

def handle_rate_limit(api_call, *args, **kwargs):
    for _ in range(3):  # Retry up to 3 times
        try:
            return api_call(*args, **kwargs)
        except Exception as e:
            log_error(f"API Rate Limit Hit: {e}")
            time.sleep(2)  # Wait and retry
    log_error("API Call Failed after 3 retries")
    raise Exception("API Call Failed after retries")
