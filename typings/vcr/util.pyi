"""
This type stub file was generated by pyright.
"""

class CaseInsensitiveDict(MutableMapping):
    """
    A case-insensitive ``dict``-like object.
    Implements all methods and operations of
    ``collections.abc.MutableMapping`` as well as dict's ``copy``. Also
    provides ``lower_items``.
    All keys are expected to be strings. The structure remembers the
    case of the last key to be set, and ``iter(instance)``,
    ``keys()``, ``items()``, ``iterkeys()``, and ``iteritems()``
    will contain case-sensitive keys. However, querying and contains
    testing is case insensitive::
        cid = CaseInsensitiveDict()
        cid['Accept'] = 'application/json'
        cid['aCCEPT'] == 'application/json'  # True
        list(cid) == ['Accept']  # True
    For example, ``headers['content-encoding']`` will return the
    value of a ``'Content-Encoding'`` response header, regardless
    of how the header name was originally stored.
    If the constructor, ``.update``, or equality comparison
    operations are given keys that have equal ``.lower()``s, the
    behavior is undefined.
    """
    def __init__(self, data=..., **kwargs) -> None:
        ...
    
    def __setitem__(self, key, value): # -> None:
        ...
    
    def __getitem__(self, key):
        ...
    
    def __delitem__(self, key): # -> None:
        ...
    
    def __iter__(self): # -> Generator[Unknown, None, None]:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def lower_items(self): # -> Generator[tuple[Unknown, Unknown], None, None]:
        """Like iteritems(), but with all lowercase keys."""
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def copy(self): # -> CaseInsensitiveDict:
        ...
    
    def __repr__(self): # -> str:
        ...
    


def partition_dict(predicate, dictionary): # -> tuple[dict[Unknown, Unknown], dict[Unknown, Unknown]]:
    ...

def compose(*functions): # -> (incoming: Unknown) -> Unknown:
    ...

def read_body(request):
    ...

def auto_decorate(decorator, predicate=...): # -> Type[DecorateAll]:
    class DecorateAll(type):
        ...
    
    

