import logging
from unittest.mock import patch

from flask import Flask

from app.utils.logger import setup_logger


def test_setup_logger():
    logger_name = "test_logger"

    logger = setup_logger(logger_name)
    assert logger.name == logger_name
    assert logger.level == logging.INFO  # Default level
    assert len(logger.handlers) > 0

    handler = logger.handlers[0]
    assert isinstance(handler, logging.StreamHandler)
    assert handler.formatter is not None
    assert handler.formatter._fmt == "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    logger_with_override = setup_logger(logger_name, level_override=logging.WARNING)
    assert logger_with_override.level == logging.WARNING

    logger.handlers.clear()  # Clear existing handlers
    logger_no_handlers = setup_logger(logger_name)
    assert len(logger_no_handlers.handlers) > 0

    invalid_level = "INVALID"
    try:
        setup_logger(logger_name, level_override=invalid_level)
    except ValueError:
        pass  # Expected behavior


def test_setup_logger_with_no_current_app():
    logger_name = "test_logger_no_app"

    with patch("flask.current_app", new=None):
        logger = setup_logger(logger_name)
        assert logger.level == logging.INFO
        assert len(logger.handlers) > 0  


def test_setup_logger_with_current_app():
    logger_name = "test_logger_with_app"

    app = Flask(__name__)
    app.config["LOG_LEVEL"] = logging.DEBUG
    with app.app_context():
        logger = setup_logger(logger_name)
        assert logger.level == logging.DEBUG 
        assert len(logger.handlers) > 0  