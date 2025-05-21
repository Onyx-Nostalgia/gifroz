import os
from typing import Optional, Tuple

import requests
from flask import Blueprint, Response, current_app, jsonify, request

from app.exceptions import NoGifFoundError, RateLimitExceededError
from app.services.giphy_service import GiphyApi
from app.services.tenor_service import TenorApi
from app.utils.logger import setup_logger

logger = setup_logger(__name__)

gif_routes = Blueprint('gif_routes', __name__)

@gif_routes.after_request
def add_no_cache_headers(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

def get_source_api(source: str) -> Tuple[Optional[object], Optional[str]]:
    api_key = None
    source_api = None

    match source:
        case "tenor":
            api_key = os.environ.get('TENOR_API_KEY')
            if not api_key:
                logger.error("TENOR_API_KEY environment variable not set")
                return None, "TENOR_API_KEY environment variable not set"
            logger.debug("Using Tenor API")
            source_api = TenorApi(api_key)
        case "giphy":
            api_key = os.environ.get('GIPHY_API_KEY')
            if not api_key:
                logger.error("GIPHY_API_KEY environment variable not set")
                return None, "GIPHY_API_KEY environment variable not set"
            logger.debug("Using Giphy API")
            source_api = GiphyApi(api_key)
        case _:
            logger.warning(f"Invalid source requested: {source}")
            return None, f"Invalid source: {source}. Choose 'tenor' or 'giphy'."

    return source_api, None

@gif_routes.route('/', methods=['GET'])
def get_gif():
    search_query = request.args.get('q', 'meme')
    source = request.args.get('source', 'GIPHY').lower()

    logger.info(f"Received request for query: '{search_query}', source: '{source}'")

    source_api, error_message = get_source_api(source)
    if error_message:
        return jsonify({"error": error_message}), 500 if "environment variable" in error_message else 400

    try:
        gif_url, detail = source_api.random_gif(search_query)
        logger.info(f"Fetched GIF URL: {gif_url}, Detail: {detail}")

        image_response = requests.get(gif_url, stream=True, timeout=10)
        image_response.raise_for_status()

        content_type = image_response.headers.get('Content-Type', 'image/gif')
        logger.debug(f"Downloaded image with Content-Type: {content_type}")

        gif_cache = current_app.config['GIF_CACHE']
        gif_cache.save(gif_url, detail, content_type, image_response.content, search_query, source)
        logger.debug("GIF saved to cache")

        return Response(image_response.content, mimetype=content_type)

    except (NoGifFoundError, RateLimitExceededError) as e:
        logger.warning(f"{type(e).__name__} occurred: {e}")
        gif_cache = current_app.config['GIF_CACHE']
        content, content_type = gif_cache.get(search_query, source)
        if content:
            return Response(content, mimetype=content_type)
        return jsonify({"error": str(e)}), 404 if isinstance(e, NoGifFoundError) else 429

    except requests.exceptions.RequestException as e:
        logger.error(f"Request error communicating with external service: {e}", exc_info=True)
        return jsonify({"error": f"Error communicating with external service: {e}"}), 503

    except Exception as e:
        logger.critical(f"An unexpected server error occurred: {type(e).__name__} - {str(e)}", exc_info=True)
        return jsonify({"error": f"An unexpected server error occurred: {type(e).__name__} - {str(e)}"}), 500
