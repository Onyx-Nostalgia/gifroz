import time
from threading import Lock

from flask import current_app


class GifCache:
    """
    A thread-safe cache for storing GIF details.
    """
    def __init__(self):
        self._cache = {
            'gif_url': None,
            'detail': None,
            'content_type': None,
            'content': None,
            'search_query': None,
            'source': None,
            'timestamp': None
        }
        self._lock = Lock()

    def save(self, gif_url, detail, content_type, content, search_query, source):
        """
        Save GIF details to the cache.
        """
        timeout = current_app.config.get('CACHE_TIMEOUT', 300)
        with self._lock:
            self._cache.update({
                'gif_url': gif_url,
                'detail': detail,
                'content_type': content_type,
                'content': content,
                'search_query': search_query,
                'source': source,
                'timestamp': time.time() + timeout
            })

    def get(self, search_query, source):
        """
        Retrieve GIF content and content type from the cache.
        """
        current_time = time.time()
        with self._lock:
            if (
                self._cache['content'] and
                self._cache['search_query'] == search_query and
                self._cache['source'] == source and
                self._cache['timestamp'] > current_time
            ):
                return self._cache['content'], self._cache['content_type']
            return None, None
