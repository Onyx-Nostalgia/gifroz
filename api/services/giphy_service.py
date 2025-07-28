import logging
import os
from typing import Dict, Tuple

from api.services.source_service import SourceApi
from api.utils.image import add_watermark_to_image_sequence


class GiphyApi(SourceApi):
    BASE_URL = "https://api.giphy.com/v1/gifs/"
    LOGO_PATH = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "assets", "giphy_logo.png")
    )
    
    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.logger = logging.getLogger(self.__class__.__name__)

    def random_gif(self, params: Dict[str, str]) -> Tuple[bytes, str]:
        search_term = params["search_term"]
        _params = {
            "api_key": self.api_key,
            "tag": search_term,
            "rating": "g",
            "limit": 1
        }

        result = self.get_request("random", params=_params)
        webp_data = result["data"]["images"].get("original", {})
        downsized_data = result["data"]["images"].get("downsized", {})

        gif_url = webp_data.get("webp")
        if not gif_url:
            self.logger.debug(f"Giphy: WebP not available for '{params}', falling back to downsized")
            gif_url = downsized_data.get("url")
        
        self.logger.debug(f"Giphy: Found WebP and downsized formats for '{params}'")
        webp_size = int(webp_data.get("webp_size", 0))
        downsized_size = int(downsized_data.get("size", 0))
        if webp_size > downsized_size:
            gif_url = downsized_data.get("url")

        detail = result["data"].get("title", "No Title")
        self.logger.debug(f"Giphy: Selected GIF URL: {gif_url}, Title: {detail}")
        image_content, content_type = self.get_image_content(gif_url)
        
        watermarked_content = add_watermark_to_image_sequence(image_content, self.LOGO_PATH)

        if watermarked_content:
            return watermarked_content, content_type

        self.logger.warning("Watermarking failed, returning original image.")
        return image_content, content_type
    
    
