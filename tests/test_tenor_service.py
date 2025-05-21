from unittest.mock import patch

from app.services.tenor_service import TenorApi


def test_tenor_random_gif():
    api = TenorApi(api_key="test_key")

    with patch.object(api, 'get_request', return_value={
        "results": [
            {
                "media_formats": {"mediumgif": {"url": "http://example.com/medium.gif"}},
                "title": "Test GIF"
            }
        ]
    }):
        gif_url, gif_name = api.random_gif("test")
        assert gif_url == "http://example.com/medium.gif"
        assert gif_name == "Test GIF"
