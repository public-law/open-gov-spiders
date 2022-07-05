"""
This type stub file was generated by pyright.
"""

import toolz
from . import operator
from toolz import apply, comp, complement, compose, compose_left, concat, concatv, count, curry, diff, first, flip, frequencies, identity, interleave, isdistinct, isiterable, juxt, last, memoize, merge_sorted, peek, pipe, second, thread_first, thread_last
from .exceptions import merge, merge_with

"""
Alternate namespace for toolz such that all functions are curried

Currying provides implicit partial evaluation of all functions

Example:

    Get usually requires two arguments, an index and a collection
    >>> from toolz.curried import get
    >>> get(0, ('a', 'b'))
    'a'

    When we use it in higher order functions we often want to pass a partially
    evaluated form
    >>> data = [(1, 2), (11, 22), (111, 222)]
    >>> list(map(lambda seq: get(0, seq), data))
    [1, 11, 111]

    The curried version allows simple expression of partial evaluation
    >>> list(map(get(0), data))
    [1, 11, 111]

See Also:
    toolz.functoolz.curry
"""
accumulate = ...
assoc = ...
assoc_in = ...
cons = ...
countby = ...
dissoc = ...
do = ...
drop = ...
excepts = ...
filter = ...
get = ...
get_in = ...
groupby = ...
interpose = ...
itemfilter = ...
itemmap = ...
iterate = ...
join = ...
keyfilter = ...
keymap = ...
map = ...
mapcat = ...
nth = ...
partial = ...
partition = ...
partition_all = ...
partitionby = ...
peekn = ...
pluck = ...
random_sample = ...
reduce = ...
reduceby = ...
remove = ...
sliding_window = ...
sorted = ...
tail = ...
take = ...
take_nth = ...
topk = ...
unique = ...
update_in = ...
valfilter = ...
valmap = ...
