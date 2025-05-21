from unittest.mock import patch

from flask import Flask

from app.utils.cache import GifCache


def test_cache_save_and_get():
    app = Flask(__name__)
    with app.app_context():
        cache = GifCache()
        gif_url = "http://example.com/gif"
        detail = "Example GIF"
        content_type = "image/gif"
        content = b"GIF89a"
        search_query = "example"
        source = "giphy"

        with patch("time.time", return_value=1000):
            cache.save(gif_url, detail, content_type, content, search_query, source)
            result = cache.get(search_query, source)
            assert result is not None
            assert result[0] == content
            assert result[1] == content_type
