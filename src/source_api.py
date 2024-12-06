from abc import ABC
from typing import Dict, Tuple

import requests


class SourceApi(ABC):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_request(self, url: str) -> Dict:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()

    def random_gif(self, search_term: str) -> Tuple[str, str]:
        raise NotImplementedError
