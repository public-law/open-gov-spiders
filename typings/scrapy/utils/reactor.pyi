"""
This type stub file was generated by pyright.
"""

def listen_tcp(portrange, host, factory): # -> None:
    """Like reactor.listenTCP but tries different ports in a range."""
    ...

class CallLaterOnce:
    """Schedule a function to be called in the next reactor loop, but only if
    it hasn't been already scheduled since the last time it ran.
    """
    def __init__(self, func, *a, **kw) -> None:
        ...
    
    def schedule(self, delay=...): # -> None:
        ...
    
    def cancel(self): # -> None:
        ...
    
    def __call__(self):
        ...
    


def install_reactor(reactor_path, event_loop_path=...): # -> None:
    """Installs the :mod:`~twisted.internet.reactor` with the specified
    import path. Also installs the asyncio event loop with the specified import
    path if the asyncio reactor is enabled"""
    ...

def verify_installed_reactor(reactor_path): # -> None:
    """Raises :exc:`Exception` if the installed
    :mod:`~twisted.internet.reactor` does not match the specified import
    path."""
    ...

def verify_installed_asyncio_event_loop(loop_path): # -> None:
    ...

def is_asyncio_reactor_installed(): # -> bool:
    ...

