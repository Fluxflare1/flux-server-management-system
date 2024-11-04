# src/backend/app/models/user.py
from sqlalchemy import Column, String
from cryptography.fernet import Fernet
from base_model import BaseModel

class User(BaseModel):
    encrypted_password = Column(String)

    def set_password(self, password):
        self.encrypted_password = Fernet.generate_key().encrypt(password.encode()).decode()

    def check_password(self, password):
        decrypted_password = Fernet.generate_key().decrypt(self.encrypted_password.encode()).decode()
        return decrypted_password == password
