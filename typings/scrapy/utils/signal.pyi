"""
This type stub file was generated by pyright.
"""

import logging

"""Helper functions for working with signals"""
logger = logging.getLogger(__name__)
class _IgnoredException(Exception):
    ...


def send_catch_log(signal=..., sender=..., *arguments, **named):
    """Like pydispatcher.robust.sendRobust but it also logs errors and returns
    Failures instead of exceptions.
    """
    ...

def send_catch_log_deferred(signal=..., sender=..., *arguments, **named):
    """Like send_catch_log but supports returning deferreds on signal handlers.
    Returns a deferred that gets fired once all signal handlers deferreds were
    fired.
    """
    ...

def disconnect_all(signal=..., sender=...):
    """Disconnect all signal handlers. Useful for cleaning up after running
    tests
    """
    ...

