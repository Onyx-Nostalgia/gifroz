from typing import Tuple

from app.source_api import SourceApi


class GiphyApi(SourceApi):
    BASE_URL = "https://api.giphy.com/v1/gifs/"

    def random_gif(self, search_term: str, limit: int = 1, rating: str = "g") -> Tuple[str, str]:
        params = {
            "api_key": self.api_key,
            "tag": search_term,
            "rating": rating,
            "limit": limit
        }

        result = self.get_request("random", params=params)

        webp_data = result["data"]["images"].get("original", {})
        downsized_data = result["data"]["images"].get("downsized", {})

        gif_url = webp_data.get("webp")
        if gif_url and downsized_data.get("url"):
            self.logger.debug(f"Giphy: Found WebP and downsized formats for '{search_term}'")
            webp_size = int(webp_data.get("webp_size", 0))
            downsized_size = int(downsized_data.get("size", 0))
            if webp_size > downsized_size:
                gif_url = downsized_data.get("url")
        elif not gif_url:
            self.logger.debug(f"Giphy: WebP not available for '{search_term}', falling back to downsized")
            gif_url = downsized_data.get("url")

        detail = result["data"].get("title", "No Title")
        self.logger.debug(f"Giphy: Selected GIF URL: {gif_url}, Title: {detail}")
        return gif_url, detail
