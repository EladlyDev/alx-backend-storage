#!/usr/bin/env python3
"""Redis practice"""
import redis
import uuid
from typing import Union


class Cache:
    """A class for caching data using Redis"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores the given data in Redis and returns the generated key"""
        key = uuid.uuid4().hex
        self._redis.set(key, data)
        return key
