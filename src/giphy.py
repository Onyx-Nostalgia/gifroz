from typing import Tuple

from src.source_api import SourceApi


class GiphyApi(SourceApi):
    def random_gif(self, search_term: str) -> Tuple[str, str]:
        url = f"https://api.giphy.com/v1/gifs/random?api_key={self.api_key}&tag={search_term}&rating=pg-13"
        result = self.get_request(url)
        gif_url = result["data"]["images"]["original"]["url"]
        detail = result["data"]["title"]
        return gif_url, detail
