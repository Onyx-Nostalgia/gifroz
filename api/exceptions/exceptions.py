class NoGifFoundError(Exception):
    """
    Raised when no GIF is found for the given query.
    """
    pass

class RateLimitExceededError(Exception):
    """
    Raised when the API rate limit is exceeded.
    """
    pass
