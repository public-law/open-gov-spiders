"""
This type stub file was generated by pyright.
"""

import contextlib
import http.client as httplib
import urllib3.connectionpool as cpool
import requests.packages.urllib3.connectionpool as cpool

"""Utilities for patching in cassettes"""
log = ...
_HTTPConnection = httplib.HTTPConnection
_HTTPSConnection = httplib.HTTPSConnection
cpool = ...
if notcpool:
    ...
class CassettePatcherBuilder:
    def __init__(self, cassette) -> None:
        ...
    
    def build(self): # -> chain[Any]:
        ...
    


class ConnectionRemover:
    def __init__(self, connection_class) -> None:
        ...
    
    def add_connection_to_pool_entry(self, pool, connection): # -> None:
        ...
    
    def remove_connection_to_pool_entry(self, pool, connection): # -> None:
        ...
    
    def __enter__(self): # -> Self@ConnectionRemover:
        ...
    
    def __exit__(self, *args): # -> None:
        ...
    


def reset_patchers(): # -> Generator[_patch[_HTTPConnection] | _patch[_HTTPSConnection] | _patch[Unknown | VerifiedHTTPSConnection] | _patch[Unknown | HTTPConnection] | _patch[Unknown | HTTPSConnection] | _patch[Unknown] | _patch[_HTTPConnectionWithTimeout] | _patch[_HTTPSConnectionWithTimeout], Any, None]:
    ...

@contextlib.contextmanager
def force_reset(): # -> Generator[None, Any, None]:
    ...

