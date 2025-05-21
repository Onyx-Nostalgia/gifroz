import logging
import os

import requests
from dotenv import load_dotenv
from flask import Flask, Response, jsonify, request
from werkzeug.exceptions import Forbidden, Unauthorized

from api.exceptions.exceptions import NoGifFoundError, RateLimitExceededError
from api.services.giphy_service import GiphyApi
from api.services.tenor_service import TenorApi
from api.utils.cache import GifCache
from api.utils.logger import setup_logger

load_dotenv()

def update_config(app: Flask):
    app.config['CLIENT_KEY'] = "gifroz"
    app.config['GIPHY_API_KEY'] = os.getenv('GIPHY_API_KEY')
    app.config['TENOR_API_KEY'] = os.getenv('TENOR_API_KEY')
    app.config['CACHE_TIMEOUT'] = int(os.getenv('CACHE_TIMEOUT', 300))
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
    app.config['LOG_LEVEL'] = getattr(logging, log_level, logging.INFO)
    return app


app = Flask(__name__)
update_config(app)
setup_logger(__name__, app.config['LOG_LEVEL'])
app.config['GIF_CACHE'] = GifCache()

@app.route('/', methods=['GET'])
def home():
    search_query = request.args.get('q', 'meme')
    source = request.args.get('source', 'GIPHY').lower()
    logger = logging.getLogger(__name__)
    logger.info(f"Search query: {search_query}, Source: {source}")
    params = {
        "client_key": app.config['CLIENT_KEY'],
        "search_term": search_query
    }

    match source:
        case "tenor":
            source_api = TenorApi(app.config['TENOR_API_KEY'])
        case "giphy":
            source_api = GiphyApi(app.config['GIPHY_API_KEY'])
        case _:
            logger.warning(f"Invalid source requested: {source}")
            return jsonify({"error": "Invalid source. Choose 'tenor' or 'giphy'."}), 400
    try:
        content, content_type = source_api.random_gif(params)
        
        # save the GIF to cache
        gif_cache = app.config['GIF_CACHE']
        gif_cache.save(content_type, content, search_query, source)
        logger.debug("GIF saved to cache")

        return Response(content, mimetype=content_type)
    except (NoGifFoundError, RateLimitExceededError) as e:
        logger.warning(f"{type(e).__name__} occurred: {e}")
        gif_cache = app.config['GIF_CACHE']
        content, content_type = gif_cache.get(search_query, source)
        if content:
            return Response(content, mimetype=content_type)
        
        # use the tenor API as a fallback 
        if source == "giphy":
            source_api = TenorApi(app.config['TENOR_API_KEY'])
            content, content_type = source_api.random_gif(params)
            gif_cache.save(content_type, content, search_query, source)
            return Response(content, mimetype=content_type)
        
        return jsonify({"error": str(e)}), 404 if isinstance(e, NoGifFoundError) else 429
    except Forbidden as e:
        return jsonify({"error": str(e) }), 403
    except Unauthorized as e:
        return jsonify({"error": str(e) }), 401
    except requests.exceptions.RequestException as e:
        logger.error(f"Request error communicating with external service: {e}", exc_info=True)
        return jsonify({"error": f"Error communicating with external service: {e}"}), 503

    except Exception as e:
        logger.critical(f"An unexpected server error occurred: {type(e).__name__} - {str(e)}", exc_info=True)
        return jsonify({"error": f"An unexpected server error occurred: {type(e).__name__} - {str(e)}"}), 500