import logging
import os
from dataclasses import dataclass


@dataclass
class BaseConfig:
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    DEBUG: bool = False
    TESTING: bool = False
    GIPHY_API_KEY: str = os.getenv('GIPHY_API_KEY')
    TENOR_API_KEY: str = os.getenv('TENOR_API_KEY')
    CACHE_TIMEOUT: int = int(os.getenv('CACHE_TIMEOUT', 300))
    LOG_LEVEL: int = logging.INFO

@dataclass
class DevelopmentConfig(BaseConfig):
    DEBUG: bool = True
    LOG_LEVEL: int = logging.DEBUG

@dataclass
class ProductionConfig(BaseConfig):
    LOG_LEVEL: int = logging.WARNING

@dataclass
class TestingConfig(BaseConfig):
    TESTING: bool = True
    DEBUG: bool = True
    LOG_LEVEL: int = logging.DEBUG
    CACHE_TIMEOUT: int = 1

def get_config_class():
    env = os.getenv('FLASK_ENV', 'development').lower()
    if env == 'production':
        return ProductionConfig
    if env == 'testing':
        return TestingConfig
    return DevelopmentConfig
