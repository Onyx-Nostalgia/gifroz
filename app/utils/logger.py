import logging
import os

DEFAULT_LOG_LEVEL_STR = os.getenv('FLASK_GLOBAL_LOG_LEVEL', 'DEBUG').upper()
DEFAULT_LOG_LEVEL_INT = getattr(logging, DEFAULT_LOG_LEVEL_STR, logging.DEBUG)


def setup_logger(name: str, level_override: int = None) -> logging.Logger:
    logger = logging.getLogger(name)

    final_level = DEFAULT_LOG_LEVEL_INT

    if level_override is not None:
        final_level = level_override
    else:
        try:
            from flask import current_app
            if current_app:
                final_level = current_app.config.get('LOG_LEVEL', DEFAULT_LOG_LEVEL_INT)
        except (ImportError, RuntimeError):
            pass

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.setLevel(final_level)
    return logger
