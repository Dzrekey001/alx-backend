#!/usr/bin/env python3
"""This module contains class that adds data to
simple dictionary"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A class for caching system"""

    def put(self, key, item):
        """Assign value to cache dictionary"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get dictionary key"""
        return self.cache_data.get(key, None)
