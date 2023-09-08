import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

class Config:
    SONGS_API_BASE_URL = os.getenv('SONGS_API_BASE_URL')
    SONGS_API_USERNAME = os.getenv('SONGS_API_USERNAME')
    SONGS_API_PASSWORD = os.getenv('SONGS_API_PASSWORD')
    REDIS_BROKER_BASE_URL = os.getenv('REDIS_BROKER_BASE_URL')