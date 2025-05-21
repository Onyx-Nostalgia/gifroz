import logging
import os


class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False
    TESTING = False
    GIPHY_API_KEY = os.getenv('GIPHY_API_KEY')
    TENOR_API_KEY = os.getenv('TENOR_API_KEY')
    CACHE_TIMEOUT = int(os.getenv('CACHE_TIMEOUT', 300))
    LOG_LEVEL = logging.INFO


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    LOG_LEVEL = logging.DEBUG


class ProductionConfig(BaseConfig):
    LOG_LEVEL = logging.WARNING 

class TestingConfig(BaseConfig):
    TESTING = True
    DEBUG = True
    LOG_LEVEL = logging.DEBUG
    CACHE_TIMEOUT = 1

def get_config_class():
    env = os.getenv('FLASK_ENV', 'development').lower()
    if env == 'production':
        return ProductionConfig
    if env == 'testing':
        return TestingConfig
    return DevelopmentConfig
