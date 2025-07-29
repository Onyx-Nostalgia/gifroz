import logging

formatter = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

def setup_logger(name: str, level_override: int = logging.INFO) -> logging.Logger:
    logging.basicConfig(level=level_override, format=formatter)
    logger = logging.getLogger(name)
    return logger