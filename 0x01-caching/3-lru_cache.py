#!/usr/bin/python3
"""lru_cache module"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU cache class"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.cache_list = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                discard = self.cache_list.pop(0)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
        self.cache_list.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            self.cache_list.remove(key)
            self.cache_list.append(key)
        return self.cache_data.get(key, None)
