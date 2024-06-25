#!/usr/bin/env python3
from base_caching import BaseCaching
from typing import Any


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching
    and implements a basic cache system
    with no limit on the number of items stored.
    """

    def __init__(self):
        """
        Initialize the BasicCache.
        Calls the parent class's __init__ method to initialize
        the cache_data dictionary.
        """
        super().__init__()

    def put(self, key: str, item: Any) -> None:
        """
        Add an item in the cache.

        Parameters:
        key (str): The key under which the item will be stored.
        item (Any): The item to be stored in the cache.

        Returns:
        None

        If either key or item is None, this method does nothing.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key: str) -> Any:
        """
        Retrieve an item from the cache.

        Parameters:
        key (str): The key corresponding to the item to be retrieved.

        Returns:
        Any: The item stored in the cache, or None if the key does not exist
        or if the key is None.
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
