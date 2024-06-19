#!/usr/bin/env python3
"""Redis practice"""
import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Retrieves the value associated with the given key from Redis.
        If a function `fn` is provided, it is applied to
        the retrieved value before returning.
        Returns the retrieved value.
        """
        val: bytes = self._redis.get(key)
        if fn:
            val = fn(val)
        return val

    def get_str(self, key: str) -> str:
        """Retrieves the string value associated with the
        given key from Redis.
        Returns the retrieved string value.
        """
        val = self._redis.get(key)
        if val:
            val = val.decode('utf-8')
        return val

    def get_int(self, key: str) -> int:
        """Retrieves the integer value associated with the
        given key from Redis.
        Returns the retrieved integer value.
        """
        val = self._redis.get(key)
        if val:
            val = int(val)
        return val
