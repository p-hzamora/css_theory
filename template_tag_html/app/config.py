import secrets

class Config:
    SECRET_KEY = secrets.token_hex(16)
    DEBUG = True
