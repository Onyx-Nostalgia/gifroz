import os


class Config:
    DEBUG = os.getenv('DEBUG', False)
    GIPHY_API_KEY = os.getenv('GIPHY_API_KEY')
    TENOR_API_KEY = os.getenv('TENOR_API_KEY')
    CACHE_TIMEOUT = int(os.getenv('CACHE_TIMEOUT', 300))
