import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path='config/environments/development.env')

# Access environment variables
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
DATABASE_URL = os.getenv('DATABASE_URL')
# etc.
