#!/usr/bin/env python3
""" Redis Cache File """
import redis
from typing import Union, Callable, Optional, Any


class Cache:
    """ Redis Caching class """

    def __init__(self):
        """ Initializes the Cache object with a redis client """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Adds data to the redis database """
        if data:
            from uuid import uuid4
            key = str(uuid4())
            value = data
            self._redis.set(key, data)
            return key or ''

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """ Given a key, fetches data from the redis client """
        data = self._redis.get(key)
        return data if not fn else fn(data)
