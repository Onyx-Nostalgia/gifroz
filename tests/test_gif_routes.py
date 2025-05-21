import pytest
from flask import Flask

from app.routes.gif_routes import gif_routes


def test_add_no_cache_headers():
    app = Flask(__name__)
    app.register_blueprint(gif_routes)

    @app.route('/test')
    def test_route():
        return "Test Response", 200

    client = app.test_client()
    response = client.get('/test')

    assert response.headers.get("Cache-Control") == "no-store, no-cache, must-revalidate, max-age=0"
    assert response.headers.get("Pragma") == "no-cache"
    assert response.headers.get("Expires") == "0"
