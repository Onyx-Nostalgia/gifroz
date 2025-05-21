from unittest.mock import MagicMock, patch

import pytest
import requests
from flask import Flask

from app.exceptions import NoGifFoundError, RateLimitExceededError
from app.routes.gif_routes import gif_routes
from app.services.giphy_service import GiphyApi
from app.services.tenor_service import TenorApi


def test_get_gif_invalid_source():
    app = Flask(__name__)
    app.register_blueprint(gif_routes)

    client = app.test_client()
    response = client.get('/?source=invalid')

    assert response.status_code == 400
    assert response.json == {"error": "Invalid source: invalid. Choose 'tenor' or 'giphy'."}

def test_get_gif_missing_api_key():
    app = Flask(__name__)
    app.register_blueprint(gif_routes)

    with patch.dict('os.environ', {"GIPHY_API_KEY": "", "TENOR_API_KEY": ""}):
        client = app.test_client()
        response = client.get('/')

        assert response.status_code == 500
        assert "environment variable not set" in response.json["error"]

def test_get_gif_no_gif_found():
    app = Flask(__name__)
    app.register_blueprint(gif_routes)

    # Add a mock GIF_CACHE to current_app.config
    with app.app_context():
        mock_gif_cache = MagicMock()
        mock_gif_cache.get.return_value = (None, None)  # Ensure it returns a tuple
        app.config['GIF_CACHE'] = mock_gif_cache

    # Simulate NoGifFoundError being raised by GiphyApi.random_gif
    with patch.object(GiphyApi, 'random_gif', side_effect=NoGifFoundError("No GIF found")):
        client = app.test_client()
        response = client.get('/?q=notfound')

        assert response.status_code == 404
        assert "No GIF found" in response.json["error"]

def test_get_gif_rate_limit_exceeded():
    app = Flask(__name__)
    app.register_blueprint(gif_routes)

    # Add a mock GIF_CACHE to current_app.config
    with app.app_context():
        mock_gif_cache = MagicMock()
        mock_gif_cache.get.return_value = (None, None)
        app.config['GIF_CACHE'] = mock_gif_cache

    # Simulate RateLimitExceededError being raised by GiphyApi.random_gif
    with patch.object(GiphyApi, 'random_gif', side_effect=RateLimitExceededError("Rate limit exceeded")):
        client = app.test_client()
        response = client.get('/?q=ratelimit')

        assert response.status_code == 429
        assert "Rate limit exceeded" in response.json["error"]

def test_get_gif_request_exception():
    app = Flask(__name__)
    app.register_blueprint(gif_routes)

    # Simulate requests.exceptions.RequestException during image download
    with patch('requests.get', side_effect=requests.exceptions.RequestException("Request failed")):
        client = app.test_client()
        response = client.get('/?q=requesterror')

        assert response.status_code == 503
        assert "Error communicating with external service" in response.json["error"]

def test_get_gif_generic_exception():
    app = Flask(__name__)
    app.register_blueprint(gif_routes)

    # Simulate a generic exception during processing
    with patch.object(GiphyApi, 'random_gif', side_effect=Exception("Unexpected error")):
        client = app.test_client()
        response = client.get('/?q=genericerror')

        assert response.status_code == 500
        assert "An unexpected server error occurred" in response.json["error"]