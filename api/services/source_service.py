import logging
from abc import ABC, abstractmethod
from typing import Any, Dict, Tuple

import requests
from werkzeug.exceptions import Forbidden, Unauthorized

from api.exceptions.exceptions import NoGifFoundError, RateLimitExceededError
from api.utils.image import add_watermark_to_image_sequence


class SourceApi(ABC):
    BASE_URL: str = ""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.logger = logging.getLogger(__name__)

    def get_request(self, endpoint: str, params: Dict = None) -> Dict:
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.get(url, params=params, timeout=10)
        match response.status_code:
            case 429:
                self.logger.warning(f"API rate limit exceeded for URL: {url}")
                raise RateLimitExceededError("API rate limit exceeded (HTTP 429). Please try again later.")
            case 403:
                self.logger.error(f"Forbidden access to URL: {url}")
                raise Forbidden("Access forbidden (HTTP 403). Check your API key and permissions.")
            case 401:
                self.logger.error(f"Unauthorized access to URL: {url}")
                raise Unauthorized("Unauthorized access (HTTP 401). Check your API key.")
        response.raise_for_status()
        data = response.json()

        if ('data' in data and not data['data']) or ('results' in data and not data['results']):
            msg = "No GIF found for the given query."
            self.logger.warning(msg)
            raise NoGifFoundError(msg)
        return data
    
    def get_image_content(self, gif_url: str) -> Tuple[str, str]:
        image_response = requests.get(gif_url, stream=True, timeout=10)
        image_response.raise_for_status()
        content_type = image_response.headers.get('Content-Type', 'image/gif')
        self.logger.info("Fetched image content successfully.")
        return image_response.content, content_type

    def _apply_watermark(
        self,
        image_content: bytes,
        logo_path: str,
        **kwargs: Any,
    ) -> bytes:
        """Applies a watermark to the image content and handles failures."""
        watermarked_content = add_watermark_to_image_sequence(
            image_content, logo_path, **kwargs
        )
        if watermarked_content:
            return watermarked_content

        self.logger.warning("Watermarking failed, returning original image.")
        return image_content

    @abstractmethod
    def random_gif(self, params: Dict[str, str]) -> Tuple[bytes, str]:
        pass
