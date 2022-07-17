"""
This type stub file was generated by pyright.
"""

from typing import Any

__all__ = ('PrettyFormat', 'pformat', 'pprint')
MYPY = ...
if MYPY:
    ...
PARENTHESES_LOOKUP = ...
DEFAULT_WIDTH = ...
MISSING = ...
PRETTY_KEY = ...
def fmt(v): # -> dict[str, Unknown]:
    ...

class SkipPretty(Exception):
    ...


@cache
def get_pygments(): # -> tuple[Module("pygments"), Any, Terminal256Formatter[Unknown]] | tuple[None, None, None]:
    ...

generator_types = ...
class PrettyFormat:
    def __init__(self, indent_step=..., indent_char=..., repr_strings=..., simple_cutoff=..., width=..., yield_from_generators=...) -> None:
        ...
    
    def __call__(self, value: Any, *, indent: int = ..., indent_first: bool = ..., highlight: bool = ...): # -> str:
        ...
    


pformat = ...
force_highlight = ...
def pprint(s, file=...): # -> None:
    ...

