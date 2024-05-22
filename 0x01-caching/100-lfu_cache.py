#!/usr/bin/python3
"""LFU Caching"""

BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """LFU Caching class"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.cache = {}
        self.keys = []
        self.count = {}

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = min(self.keys, key=lambda k: self.count.get(k, 0))
            self.cache_data.pop(discard)
            self.count.pop(discard)
            self.keys.remove(discard)
            print("DISCARD: {}".format(discard))
        self.cache_data[key] = item
        if key in self.keys:
            self.keys.remove(key)
        self.keys.append(key)
        self.count[key] = self.count.get(key, 0) + 1

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            self.count[key] = self.count.get(key, 0) + 1
            self.keys.remove(key)
            self.keys.append(key)
        return self.cache_data.get(key, None)
