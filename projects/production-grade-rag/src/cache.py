import time
from threading import Lock


class ResponseCache:
    def __init__(self, ttl_seconds=300):
        self.ttl_seconds = ttl_seconds
        self._cache = {}
        self._lock = Lock()

    def get(self, key):
        with self._lock:
            item = self._cache.get(key)

            if item is None:
                return None

            value, expires_at = item

            if time.monotonic() >= expires_at:
                del self._cache[key]
                return None

            return value

    def set(self, key, value):
        with self._lock:
            self._cache[key] = (
                value,
                time.monotonic() + self.ttl_seconds,
            )


response_cache = ResponseCache(ttl_seconds=300)
