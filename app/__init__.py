import logging
import os

from flask import Flask

from app.config import get_config_class
from app.utils.cache import GifCache


def create_app(config_name_override=None):
    app = Flask(__name__)

    if config_name_override:
        from app import config as app_config
        if config_name_override == 'production':
            config_object = app_config.ProductionConfig
        elif config_name_override == 'testing':
            config_object = app_config.TestingConfig
        else:
            config_object = app_config.DevelopmentConfig
    else:
        config_object = get_config_class()

    app.config.from_object(config_object)

    app.config['GIF_CACHE'] = GifCache()

    if not app.logger.handlers or os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        stream_handler.setFormatter(formatter)
        app.logger.handlers.clear()
        app.logger.addHandler(stream_handler)
        app.logger.setLevel(app.config.get('LOG_LEVEL', logging.INFO))

    from app.routes.gif_routes import gif_routes
    env = os.environ.get('FLASK_ENV')
    app.register_blueprint(gif_routes)
    app.logger.info(f"Application created in '{env}' mode using {config_object.__name__}.")
    if not app.config.get('GIPHY_API_KEY') and not app.config.get('TENOR_API_KEY'):
        app.logger.warning("Neither GIPHY_API_KEY nor TENOR_API_KEY are set. GIF functionality might be limited.")

    return app
