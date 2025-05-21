from unittest.mock import patch

from app.services.giphy_service import GiphyApi


def test_giphy_random_gif():
    api = GiphyApi(api_key="test_key")

    with patch.object(api, 'get_request', return_value={
        "data": {
            "images": {
                "original": {"webp": "http://example.com/original.webp", "webp_size": "2000"},
                "downsized": {"url": "http://example.com/downsized.gif", "size": "1000"}
            },
            "title": "Test GIF"
        }
    }):
        gif_url, detail = api.random_gif("test")
        assert gif_url == "http://example.com/downsized.gif"
        assert detail == "Test GIF"
