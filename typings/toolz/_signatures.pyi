"""
This type stub file was generated by pyright.
"""

"""Internal module for better introspection of builtins.

The main functions are ``is_builtin_valid_args``, ``is_builtin_partial_args``,
and ``has_unknown_args``.  Other functions in this module support these three.

Notably, we create a ``signatures`` registry to enable introspection of
builtin functions in any Python version.  This includes builtins that
have more than one valid signature.  Currently, the registry includes
builtins from ``builtins``, ``functools``, ``itertools``, and ``operator``
modules.  More can be added as requested.  We don't guarantee full coverage.

Everything in this module should be regarded as implementation details.
Users should try to not use this module directly.
"""
module_info = ...
def num_pos_args(sigspec): # -> int:
    """ Return the number of positional arguments.  ``f(x, y=1)`` has 1"""
    ...

def get_exclude_keywords(num_pos_only, sigspec): # -> tuple[()] | tuple[Unknown, ...]:
    """ Return the names of position-only arguments if func has **kwargs"""
    ...

def signature_or_spec(func): # -> Signature | None:
    ...

def expand_sig(sig): # -> tuple[Unknown | int, Unknown, Unknown | tuple[Any, ...], Signature | None]:
    """ Convert the signature spec in ``module_info`` to add to ``signatures``

    The input signature spec is one of:
        - ``lambda_func``
        - ``(num_position_args, lambda_func)``
        - ``(num_position_args, lambda_func, keyword_only_args)``

    The output signature spec is:
        ``(num_position_args, lambda_func, keyword_exclude, sigspec)``

    where ``keyword_exclude`` includes keyword only arguments and, if variadic
    keywords is present, the names of position-only argument.  The latter is
    included to support builtins such as ``partial(func, *args, **kwargs)``,
    which allows ``func=`` to be used as a keyword even though it's the name
    of a positional argument.
    """
    ...

signatures = ...
def create_signature_registry(module_info=..., signatures=...): # -> None:
    ...

def check_valid(sig, args, kwargs): # -> bool:
    """ Like ``is_valid_args`` for the given signature spec"""
    ...

def check_partial(sig, args, kwargs):
    """ Like ``is_partial_args`` for the given signature spec"""
    ...

def check_arity(n, sig): # -> bool | None:
    ...

def check_varargs(sig): # -> bool | None:
    ...

def check_keywords(sig): # -> bool | None:
    ...

def check_required_args(sig): # -> int | Literal[False] | None:
    ...

