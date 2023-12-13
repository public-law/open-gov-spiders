"""
This type stub file was generated by pyright.
"""

from asyncio import AbstractEventLoop, AbstractEventLoopPolicy
from typing import Any, Callable, Optional

def listen_tcp(portrange, host, factory): # -> None:
    """Like reactor.listenTCP but tries different ports in a range."""
    ...

class CallLaterOnce:
    """Schedule a function to be called in the next reactor loop, but only if
    it hasn't been already scheduled since the last time it ran.
    """
    def __init__(self, func: Callable, *a: Any, **kw: Any) -> None:
        ...
    
    def schedule(self, delay: float = ...) -> None:
        ...
    
    def cancel(self) -> None:
        ...
    
    def __call__(self) -> Any:
        ...
    


def set_asyncio_event_loop_policy() -> None:
    """The policy functions from asyncio often behave unexpectedly,
    so we restrict their use to the absolutely essential case.
    This should only be used to install the reactor.
    """
    ...

def get_asyncio_event_loop_policy() -> AbstractEventLoopPolicy:
    ...

def install_reactor(reactor_path: str, event_loop_path: Optional[str] = ...) -> None:
    """Installs the :mod:`~twisted.internet.reactor` with the specified
    import path. Also installs the asyncio event loop with the specified import
    path if the asyncio reactor is enabled"""
    ...

def set_asyncio_event_loop(event_loop_path: Optional[str]) -> AbstractEventLoop:
    """Sets and returns the event loop with specified import path."""
    ...

def verify_installed_reactor(reactor_path: str) -> None:
    """Raises :exc:`Exception` if the installed
    :mod:`~twisted.internet.reactor` does not match the specified import
    path."""
    ...

def verify_installed_asyncio_event_loop(loop_path: str) -> None:
    ...

def is_asyncio_reactor_installed() -> bool:
    ...

