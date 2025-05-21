from typing import Tuple

from app.source_api import SourceApi
from app.utils.logger import setup_logger


class TenorApi(SourceApi):
    BASE_URL = "https://tenor.googleapis.com/v2/"
    CLIENT_KEY = "gifroz"

    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.logger = setup_logger(self.__class__.__name__)

    def random_gif(self, search_term: str, limit: int = 1) -> Tuple[str, str]:
        params = {
            "q": search_term,
            "key": self.api_key,
            "client_key": self.CLIENT_KEY,
            "limit": limit,
            "media_filter": "mediumgif",
            "random": "true"
        }

        result = self.get_request("search", params=params)
        gif_data = result["results"][0]
        gif_url = gif_data["media_formats"]["mediumgif"]["url"]
        gif_name = gif_data.get("title") or self.get_gif_name(gif_url)
        self.logger.debug(f"Tenor: Selected GIF URL: {gif_url}, Title: {gif_name}")
        return gif_url, gif_name

    @staticmethod
    def get_gif_name(gif_url: str) -> str:
        start_index = gif_url.rfind("/")
        if (start_index == -1):
            raise ValueError("Invalid GIF URL")
        return gif_url[start_index + 1:]
