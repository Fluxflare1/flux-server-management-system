import logging
from logging.handlers import RotatingFileHandler

# Logger setup
logger = logging.getLogger("FluxLogger")
logger.setLevel(logging.DEBUG)

# Rotating file handler (log file rotation)
handler = RotatingFileHandler("logs/flux_server.log", maxBytes=5 * 1024 * 1024, backupCount=3)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(handler)

# Example usage
def log_error(error_message):
    logger.error(error_message)
