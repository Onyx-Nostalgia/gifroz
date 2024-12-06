from typing import Tuple

from src.source_api import SourceApi


class TenorApi(SourceApi):
    def random_gif(self, search_term: str, limit: int = 1) -> Tuple[str, str]:
        url = f"https://g.tenor.com/v1/random?q={search_term}&key={self.api_key}&limit={limit}&ar_range=standard&media_filter=minimal"
        result = self.get_request(url)
        result = result["results"][0]
        gif_url = result["media"][0]["gif"]["url"]
        gif_name = self.get_gif_name(gif_url)
        return gif_url, gif_name

    @staticmethod
    def get_gif_name(gif_url: str) -> str:
        start_index = gif_url.rfind("/")
        if start_index == -1:
            raise ValueError("Invalid GIF URL")
        gif_name = gif_url[start_index + 1 :]
        return gif_name
