"""
This type stub file was generated by pyright.
"""

import collections
import six
from abc import ABCMeta
from scrapy.utils.trackref import object_ref

"""
Scrapy Item

See documentation in docs/topics/item.rst
"""
if six.PY2:
    MutableMapping = collections.MutableMapping
else:
    MutableMapping = collections.abc.MutableMapping
class BaseItem(object_ref):
    """Base class for all scraped items.

    In Scrapy, an object is considered an *item* if it is an instance of either
    :class:`BaseItem` or :class:`dict`. For example, when the output of a
    spider callback is evaluated, only instances of :class:`BaseItem` or
    :class:`dict` are passed to :ref:`item pipelines <topics-item-pipeline>`.

    If you need instances of a custom class to be considered items by Scrapy,
    you must inherit from either :class:`BaseItem` or :class:`dict`.

    Unlike instances of :class:`dict`, instances of :class:`BaseItem` may be
    :ref:`tracked <topics-leaks-trackrefs>` to debug memory leaks.
    """
    ...


class Field(dict):
    """Container of field metadata"""
    ...


class ItemMeta(ABCMeta):
    """Metaclass_ of :class:`Item` that handles field definitions.

    .. _metaclass: https://realpython.com/python-metaclasses
    """
    def __new__(mcs, class_name, bases, attrs):
        ...
    


class DictItem(MutableMapping, BaseItem):
    fields = ...
    def __new__(cls, *args, **kwargs):
        ...
    
    def __init__(self, *args, **kwargs):
        ...
    
    def __getitem__(self, key):
        ...
    
    def __setitem__(self, key, value):
        ...
    
    def __delitem__(self, key):
        ...
    
    def __getattr__(self, name):
        ...
    
    def __setattr__(self, name, value):
        ...
    
    def __len__(self):
        ...
    
    def __iter__(self):
        ...
    
    __hash__ = ...
    def keys(self):
        ...
    
    def __repr__(self):
        ...
    
    def copy(self):
        ...
    
    def deepcopy(self):
        """Return a `deep copy`_ of this item.

        .. _deep copy: https://docs.python.org/library/copy.html#copy.deepcopy
        """
        ...
    


@six.add_metaclass(ItemMeta)
class Item(DictItem):
    ...


