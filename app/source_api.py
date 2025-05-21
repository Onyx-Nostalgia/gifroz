from abc import ABC, abstractmethod
from typing import Dict, Tuple

import requests

from app.exceptions import NoGifFoundError, RateLimitExceededError
from app.utils.logger import setup_logger

logger = setup_logger(__name__)

class SourceApi(ABC):
    BASE_URL: str = ""

    def __init__(self, api_key: str, logger=logger):
        self.api_key = api_key
        self.logger = logger

    def get_request(self, endpoint: str, params: Dict = None) -> Dict:
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 429:
            self.logger.warning(f"API rate limit exceeded for URL: {url}")
            raise RateLimitExceededError("API rate limit exceeded (HTTP 429). Please try again later.")
        response.raise_for_status()
        data = response.json()

        if 'data' in data and not data['data']:
            self.logger.warning(f"No GIF found in response for URL: {url}")
            raise NoGifFoundError("No GIF found for the given query.")
        if 'results' in data and not data['results']:
            self.logger.warning(f"No GIF found in response for URL: {url} (using 'results' key)")
            raise NoGifFoundError("No GIF found for the given query.")

        return data

    @abstractmethod
    def random_gif(self, search_term: str) -> Tuple[str, str]:
        pass
