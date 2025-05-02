from cryptography.fernet import Fernet
import os

# Normally you'd generate and store this securely
FERNET_KEY = os.environ.get("FERNET_KEY", Fernet.generate_key())
fernet = Fernet(FERNET_KEY)

def encrypt_data(data: str) -> str:
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(token: str) -> str:
    return fernet.decrypt(token.encode()).decode()
