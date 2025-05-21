import logging
from abc import ABC, abstractmethod
from typing import Dict, Tuple

import requests

from api.exceptions.exceptions import NoGifFoundError, RateLimitExceededError


class SourceApi(ABC):
    BASE_URL: str = ""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.logger = logging.getLogger(__name__)

    def get_request(self, endpoint: str, params: Dict = None) -> Dict:
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 429:
            self.logger.warning(f"API rate limit exceeded for URL: {url}")
            raise RateLimitExceededError("API rate limit exceeded (HTTP 429). Please try again later.")
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

    @abstractmethod
    def random_gif(self, search_term: str) -> Tuple[str, str]:
        pass
