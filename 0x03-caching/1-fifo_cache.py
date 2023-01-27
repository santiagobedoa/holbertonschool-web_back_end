#!/usr/bin/env python3
"""1. FIFO caching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    FIFOCache that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """Initialize"""
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache using FIFO algorithm"""
        if key and item:
            if self.MAX_ITEMS > 0:
                self.cache_data[key] = item
                self.MAX_ITEMS -= 1

            else:
                self.cache_data.popitem(last=False)
                self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key and self.cache_data.get(key):
            return self.cache_data.get(key)
        else:
            return None
