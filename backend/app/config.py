# backend/app/config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/twix_ai'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
