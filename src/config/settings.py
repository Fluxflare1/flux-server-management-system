
import os
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = os.path.join('config/environments', 'development.env')
load_dotenv(dotenv_path=env_path)

# Environment configurations
AUTO_OS_UPDATE_ENABLED = os.getenv('AUTO_OS_UPDATE_ENABLED', 'false').lower() == 'true'
OS_UPDATE_INTERVAL_DAYS = int(os.getenv('OS_UPDATE_INTERVAL_DAYS', 7))

# Linux configurations
LINUX_PACKAGE_MANAGER = os.getenv('LINUX_PACKAGE_MANAGER', 'apt')
LINUX_UPDATE_COMMAND = os.getenv('LINUX_UPDATE_COMMAND', 'sudo apt update && sudo apt upgrade -y')
LINUX_INSTALL_COMMAND = os.getenv('LINUX_INSTALL_COMMAND', 'sudo apt install -y')

# Windows configurations
WINDOWS_PACKAGE_MANAGER = os.getenv('WINDOWS_PACKAGE_MANAGER', 'choco')
WINDOWS_UPDATE_COMMAND = os.getenv('WINDOWS_UPDATE_COMMAND', 'choco upgrade all -y')
WINDOWS_INSTALL_COMMAND = os.getenv('WINDOWS_INSTALL_COMMAND', 'choco install')




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
