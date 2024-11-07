import os
from dotenv import load_dotenv

# Load the appropriate environment file
environment = os.getenv("ENVIRONMENT", "development")
env_path = f"config/environments/{environment}.env"
load_dotenv(env_path)

# Usage examples:
SERVER_HOST = os.getenv("SERVER_HOST", "localhost")
SERVER_PORT = os.getenv("SERVER_PORT", "8000")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
API_KEY = os.getenv("API_KEY")
