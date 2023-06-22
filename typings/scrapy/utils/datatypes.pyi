"""
This type stub file was generated by pyright.
"""

import collections
import weakref

"""
This module contains data types used by Scrapy which are not included in the
Python Standard Library.

This module must not depend on any module outside the Standard Library.
"""
class CaselessDict(dict):
    __slots__ = ...
    def __init__(self, seq=...) -> None:
        ...
    
    def __getitem__(self, key):
        ...
    
    def __setitem__(self, key, value): # -> None:
        ...
    
    def __delitem__(self, key): # -> None:
        ...
    
    def __contains__(self, key): # -> bool:
        ...
    
    has_key = ...
    def __copy__(self): # -> CaselessDict:
        ...
    
    copy = ...
    def normkey(self, key):
        """Method to normalize dictionary key access"""
        ...
    
    def normvalue(self, value):
        """Method to normalize values prior to be set"""
        ...
    
    def get(self, key, def_val=...): # -> None:
        ...
    
    def setdefault(self, key, def_val=...): # -> None:
        ...
    
    def update(self, seq): # -> None:
        ...
    
    @classmethod
    def fromkeys(cls, keys, value=...): # -> Self@CaselessDict:
        ...
    
    def pop(self, key, *args):
        ...
    


class LocalCache(collections.OrderedDict):
    """Dictionary with a finite number of keys.

    Older items expires first.
    """
    def __init__(self, limit=...) -> None:
        ...
    
    def __setitem__(self, key, value): # -> None:
        ...
    


class LocalWeakReferencedCache(weakref.WeakKeyDictionary):
    """
    A weakref.WeakKeyDictionary implementation that uses LocalCache as its
    underlying data structure, making it ordered and capable of being size-limited.

    Useful for memoization, while avoiding keeping received
    arguments in memory only because of the cached references.

    Note: like LocalCache and unlike weakref.WeakKeyDictionary,
    it cannot be instantiated with an initial dictionary.
    """
    def __init__(self, limit=...) -> None:
        ...
    
    def __setitem__(self, key, value): # -> None:
        ...
    
    def __getitem__(self, key): # -> None:
        ...
    


class SequenceExclude:
    """Object to test if an item is NOT within some sequence."""
    def __init__(self, seq) -> None:
        ...
    
    def __contains__(self, item): # -> bool:
        ...
    


