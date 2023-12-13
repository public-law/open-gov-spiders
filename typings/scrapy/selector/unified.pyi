"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional
from parsel import Selector as _ParselSelector
from scrapy.http import TextResponse
from scrapy.utils.trackref import object_ref

"""
XPath selectors based on lxml
"""
__all__ = ["Selector", "SelectorList"]
_NOT_SET = ...
class SelectorList(_ParselSelector.selectorlist_cls, object_ref):
    """
    The :class:`SelectorList` class is a subclass of the builtin ``list``
    class, which provides a few additional methods.
    """
    ...


class Selector(_ParselSelector, object_ref):
    """
    An instance of :class:`Selector` is a wrapper over response to select
    certain parts of its content.

    ``response`` is an :class:`~scrapy.http.HtmlResponse` or an
    :class:`~scrapy.http.XmlResponse` object that will be used for selecting
    and extracting data.

    ``text`` is a unicode string or utf-8 encoded text for cases when a
    ``response`` isn't available. Using ``text`` and ``response`` together is
    undefined behavior.

    ``type`` defines the selector type, it can be ``"html"``, ``"xml"``
    or ``None`` (default).

    If ``type`` is ``None``, the selector automatically chooses the best type
    based on ``response`` type (see below), or defaults to ``"html"`` in case it
    is used together with ``text``.

    If ``type`` is ``None`` and a ``response`` is passed, the selector type is
    inferred from the response type as follows:

    * ``"html"`` for :class:`~scrapy.http.HtmlResponse` type
    * ``"xml"`` for :class:`~scrapy.http.XmlResponse` type
    * ``"html"`` for anything else

    Otherwise, if ``type`` is set, the selector type will be forced and no
    detection will occur.
    """
    __slots__ = ...
    selectorlist_cls = SelectorList
    def __init__(self, response: Optional[TextResponse] = ..., text: Optional[str] = ..., type: Optional[str] = ..., root: Optional[Any] = ..., **kwargs: Any) -> None:
        ...
    


