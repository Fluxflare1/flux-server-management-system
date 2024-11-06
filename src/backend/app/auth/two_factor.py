# src/backend/auth/two_factor.py

import random
import time
from src.backend.utils.email_service import send_email

class TwoFactorAuth:
    codes = {}

    @staticmethod
    def generate_code(user_id):
        code = random.randint(100000, 999999)
        expiration = time.time() + 300  # Code valid for 5 minutes
        TwoFactorAuth.codes[user_id] = {'code': code, 'expires': expiration}
        return code

    @staticmethod
    def validate_code(user_id, code):
        if user_id in TwoFactorAuth.codes:
            if TwoFactorAuth.codes[user_id]['code'] == code and time.time() < TwoFactorAuth.codes[user_id]['expires']:
                del TwoFactorAuth.codes[user_id]  # Remove code after successful validation
                return True
        return False

    @staticmethod
    def send_code(user_id, email):
        code = TwoFactorAuth.generate_code(user_id)
        message = f"Your verification code is: {code}"
        send_email(email, "Two-Factor Authentication Code", message)
