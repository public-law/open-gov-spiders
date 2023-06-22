"""
This type stub file was generated by pyright.
"""

from contextlib import contextmanager

"""Helper functions which don't fit anywhere else"""
_ITERABLE_SINGLE_VALUES = ...
def arg_to_iter(arg): # -> list[Unknown] | list[dict[Unknown, Unknown] | Item | str | bytes | Unknown]:
    """Convert an argument to an iterable. The argument can be a None, single
    value, or an iterable.

    Exception: if arg is a dict, [arg] will be returned
    """
    ...

def load_object(path): # -> Any:
    """Load an object given its absolute object path, and return it.

    The object can be the import path of a class, function, variable or an
    instance, e.g. 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware'.

    If ``path`` is not a string, but is a callable object, such as a class or
    a function, then return it as is.
    """
    ...

def walk_modules(path): # -> list[Unknown]:
    """Loads a module and all its submodules from the given module path and
    returns them. If *any* module throws an exception while importing, that
    exception is thrown back.

    For example: walk_modules('scrapy.utils')
    """
    ...

def extract_regex(regex, text, encoding=...): # -> list[str]:
    """Extract a list of unicode strings from the given text/encoding using the following policies:

    * if the regex contains a named group called "extract" that will be returned
    * if the regex contains multiple numbered groups, all those will be returned (flattened)
    * if the regex doesn't contain any group the entire regex matching is returned
    """
    ...

def md5sum(file): # -> str:
    """Calculate the md5 checksum of a file-like object without reading its
    whole content in memory.

    >>> from io import BytesIO
    >>> md5sum(BytesIO(b'file content to hash'))
    '784406af91dd5a54fbb9c84c2236595a'
    """
    ...

def rel_has_nofollow(rel): # -> bool:
    """Return True if link rel attribute has nofollow type"""
    ...

def create_instance(objcls, settings, crawler, *args, **kwargs):
    """Construct a class instance using its ``from_crawler`` or
    ``from_settings`` constructors, if available.

    At least one of ``settings`` and ``crawler`` needs to be different from
    ``None``. If ``settings `` is ``None``, ``crawler.settings`` will be used.
    If ``crawler`` is ``None``, only the ``from_settings`` constructor will be
    tried.

    ``*args`` and ``**kwargs`` are forwarded to the constructors.

    Raises ``ValueError`` if both ``settings`` and ``crawler`` are ``None``.

    .. versionchanged:: 2.2
       Raises ``TypeError`` if the resulting instance is ``None`` (e.g. if an
       extension has not been implemented correctly).
    """
    ...

@contextmanager
def set_environ(**kwargs): # -> Generator[None, Any, None]:
    """Temporarily set environment variables inside the context manager and
    fully restore previous environment afterwards
    """
    ...

def walk_callable(node): # -> Generator[FunctionDef | Unknown, Any, None]:
    """Similar to ``ast.walk``, but walks only function body and skips nested
    functions defined within the node.
    """
    ...

_generator_callbacks_cache = ...
def is_generator_with_return_value(callable): # -> None:
    """
    Returns True if a callable is a generator function which includes a
    'return' statement with a value different than None, False otherwise
    """
    ...

def warn_on_generator_with_return_value(spider, callable): # -> None:
    """
    Logs a warning if a callable is a generator function and includes
    a 'return' statement with a value different than None
    """
    ...

