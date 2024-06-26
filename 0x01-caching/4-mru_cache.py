#!/usr/bin/env python3
"""Most Recently used caching module.
"""
from collections import OrderedDict
from base_caching import BaseCaching
from typing import Any


class MRUCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a MRU
    removal mechanism when the limit is reached.
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key: str, item: Any) -> Any:
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                print("DISCARD:", first_key)
                del self.cache_data[first_key]
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=False)

    def get(self, key: str) -> Any:
        """Retrieves an item by key.
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
            return self.cache_data[key]
        return None
