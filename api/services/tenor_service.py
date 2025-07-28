import logging
import os
from typing import Dict, Tuple

from api.services.source_service import SourceApi
from api.utils.image import add_watermark_to_image_sequence


class TenorApi(SourceApi):
    BASE_URL = "https://tenor.googleapis.com/v2/"
    LOGO_PATH = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "assets", "tenor_logo.png")
    )

    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.logger = logging.getLogger(self.__class__.__name__)

    def random_gif(self, params: Dict[str, str]) -> Tuple[bytes, str]:
        search_term = params["search_term"]
        client_key = params.get("client_key")
        _params = {
            "q": search_term,
            "key": self.api_key,
            "client_key": client_key,
            "limit": 1,
            "media_filter": "mediumgif",
            "random": "true"
        }
        result = self.get_request("search", params=_params)
        gif_data = result["results"][0]
        gif_url = gif_data["media_formats"]["mediumgif"]["url"]
        gif_name = gif_data.get("title") or self.get_gif_name(gif_url)
        self.logger.debug(f"Tenor: Selected GIF URL: {gif_url}, Title: {gif_name}")
        image_content, content_type = self.get_image_content(gif_url)
        
        watermarked_content = add_watermark_to_image_sequence(image_content, self.LOGO_PATH, padding=2,opacity=1.0)

        if watermarked_content:
            return watermarked_content, content_type

        self.logger.warning("Watermarking failed, returning original image.")
        return image_content, content_type

    @staticmethod
    def get_gif_name(gif_url: str) -> str:
        start_index = gif_url.rfind("/")
        if (start_index == -1):
            raise ValueError("Invalid GIF URL")
        return gif_url[start_index + 1:]
