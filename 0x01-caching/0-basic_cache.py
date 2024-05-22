#!/usr/bin/python3
"""Basic Cache module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic Cache class"""

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key)
