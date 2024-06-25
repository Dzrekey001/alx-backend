#!/usr/bin/env python3
from base_caching import BaseCaching
from typing import Any


class FIFOCache(BaseCaching):
    """
    FIFOCache class inherits from BaseCaching and implements
    a First-In-First-Out (FIFO) caching strategy.

    Attributes:
        Inherits MAX_ITEMS and cache_data from BaseCaching.

    Methods:
        put(key: str, item: Any) -> None:
            Adds a key-value pair to the cache. If the cache
            exceeds MAX_ITEMS, it removes the oldest item.
        get(key: str) -> Any:
            Retrieves the value associated with the given key from the cache.

    Usage:
        cache = FIFOCache()
        cache.put('key1', 'value1')
        value = cache.get('key1')
        print(value)  # Output: 'value1'
    """

    def __init__(self):
        """
        Initializes an instance of FIFOCache.
        """
        super().__init__()

    def put(self, key: str, item: Any) -> None:
        """
        Adds a key-value pair to the cache. If the cache exceeds MAX_ITEMS,
        it removes the oldest item.

        Args:
            key (str): The key for the item to be cached.
            item (Any): The item (value) to be cached.

        Returns:
            None
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            oldest_key = next(iter(self.cache_data))
            del self.cache_data[oldest_key]
            print("DISCARD:", oldest_key)

    def get(self, key: str) -> Any:
        """
        Retrieves the value associated with the given key from the cache.

        Args:
            key (str): The key whose value is to be retrieved.

        Returns:
            Any: The value associated with the key if present, otherwise None.
        """
        if key is None:
            return None

        return self.cache_data.get(key, None)
