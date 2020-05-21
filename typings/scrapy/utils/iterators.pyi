"""
This type stub file was generated by pyright.
"""

import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)
def xmliter(obj, nodename):
    """Return a iterator of Selector's over all nodes of a XML document,
       given the name of the node to iterate. Useful for parsing XML feeds.

    obj can be:
    - a Response object
    - a unicode string
    - a string encoded as utf-8
    """
    ...

def xmliter_lxml(obj, nodename, namespace: Optional[Any] = ..., prefix=...):
    ...

class _StreamReader(object):
    def __init__(self, obj):
        ...
    
    def read(self, n=...):
        self.read = ...
    
    def _read_string(self, n=...):
        ...
    
    def _read_unicode(self, n=...):
        ...
    


def csviter(obj, delimiter: Optional[Any] = ..., headers: Optional[Any] = ..., encoding: Optional[Any] = ..., quotechar: Optional[Any] = ...):
    """ Returns an iterator of dictionaries from the given csv object

    obj can be:
    - a Response object
    - a unicode string
    - a string encoded as utf-8

    delimiter is the character used to separate fields on the given obj.

    headers is an iterable that when provided offers the keys
    for the returned dictionaries, if not the first row is used.

    quotechar is the character used to enclosure fields on the given obj.
    """
    ...

def _body_or_str(obj, unicode: bool = ...):
    ...

