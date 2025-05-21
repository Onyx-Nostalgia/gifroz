# import os
# from unittest.mock import patch

# import pytest
# from dotenv import load_dotenv


# @pytest.fixture(autouse=True)
# def load_test_env():
#     os.environ.clear()
#     load_dotenv(dotenv_path="./.env.test", override=True)

# def test_base_config():
#     load_dotenv(dotenv_path="./.env.test", override=True)
#     from app.config import BaseConfig
#     config = BaseConfig()
#     assert config.SECRET_KEY == 'test_secret_key'
#     assert config.DEBUG is False
#     assert config.TESTING is False
#     assert config.CACHE_TIMEOUT == 300

# def test_development_config():
#     from app.config import DevelopmentConfig
#     config = DevelopmentConfig()
#     assert config.DEBUG is True
#     assert config.LOG_LEVEL == 10  # DEBUG level

# def test_production_config():
#     from app.config import ProductionConfig
#     config = ProductionConfig()
#     assert config.LOG_LEVEL == 30  # WARNING level

# def test_testing_config():
#     from app.config import TestingConfig
#     config = TestingConfig()
#     assert config.TESTING is True
#     assert config.DEBUG is True
#     assert config.CACHE_TIMEOUT == 1

# def test_get_config_class():
#     from app.config import (
#         DevelopmentConfig,
#         ProductionConfig,
#         TestingConfig,
#         get_config_class,
#     )
#     with patch.dict(os.environ, {"FLASK_ENV": "production"}):
#         assert get_config_class() == ProductionConfig

#     with patch.dict(os.environ, {"FLASK_ENV": "testing"}):
#         assert get_config_class() == TestingConfig

#     with patch.dict(os.environ, {"FLASK_ENV": "development"}):
#         assert get_config_class() == DevelopmentConfig

#     with patch.dict(os.environ, {"FLASK_ENV": "unknown"}):
#         assert get_config_class() == DevelopmentConfig
