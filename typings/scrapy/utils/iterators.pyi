"""
This type stub file was generated by pyright.
"""

logger = ...
def xmliter(obj, nodename): # -> Generator[Selector, Any, None]:
    """Return a iterator of Selector's over all nodes of a XML document,
       given the name of the node to iterate. Useful for parsing XML feeds.

    obj can be:
    - a Response object
    - a unicode string
    - a string encoded as utf-8
    """
    ...

def xmliter_lxml(obj, nodename, namespace=..., prefix=...): # -> Generator[SelectorList | Unknown, Any, None]:
    ...

class _StreamReader:
    def __init__(self, obj) -> None:
        ...
    
    def read(self, n=...): # -> Any:
        ...
    


def csviter(obj, delimiter=..., headers=..., encoding=..., quotechar=...): # -> Generator[dict[str | Unknown, str | Unknown], Any, None]:
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

