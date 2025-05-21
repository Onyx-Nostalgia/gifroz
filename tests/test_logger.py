import logging

from app.utils.logger import setup_logger


def test_setup_logger():
    logger_name = "test_logger"
    logger = setup_logger(logger_name)

    assert logger.name == logger_name
    assert logger.level == logging.DEBUG  # Default level
    assert len(logger.handlers) > 0

    # Test with level override
    logger_with_override = setup_logger(logger_name, level_override=logging.WARNING)
    assert logger_with_override.level == logging.WARNING
