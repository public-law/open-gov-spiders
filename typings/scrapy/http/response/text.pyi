"""
This type stub file was generated by pyright.
"""

from typing import Any, Generator, TYPE_CHECKING, Tuple
from scrapy.http import Request
from scrapy.http.response import Response

"""
This module implements the TextResponse class which adds encoding handling and
discovering (through HTTP headers) to base Response class.

See documentation in docs/topics/request-response.rst
"""
if TYPE_CHECKING:
    ...
_NONE = ...
class TextResponse(Response):
    _DEFAULT_ENCODING = ...
    _cached_decoded_json = ...
    attributes: Tuple[str, ...] = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        ...
    
    @property
    def encoding(self): # -> Any | str:
        ...
    
    def json(self): # -> Any | object:
        """
        .. versionadded:: 2.2

        Deserialize a JSON document to a Python object.
        """
        ...
    
    @property
    def text(self) -> str:
        """Body as unicode"""
        ...
    
    def urljoin(self, url): # -> str:
        """Join this Response's url with a possible relative url to form an
        absolute interpretation of the latter."""
        ...
    
    @property
    def selector(self): # -> Selector:
        ...
    
    def jmespath(self, query, **kwargs): # -> SelectorList[Selector]:
        ...
    
    def xpath(self, query, **kwargs): # -> SelectorList[Selector]:
        ...
    
    def css(self, query): # -> SelectorList[Selector]:
        ...
    
    def follow(self, url, callback=..., method=..., headers=..., body=..., cookies=..., meta=..., encoding=..., priority=..., dont_filter=..., errback=..., cb_kwargs=..., flags=...) -> Request:
        """
        Return a :class:`~.Request` instance to follow a link ``url``.
        It accepts the same arguments as ``Request.__init__`` method,
        but ``url`` can be not only an absolute URL, but also

        * a relative URL
        * a :class:`~scrapy.link.Link` object, e.g. the result of
          :ref:`topics-link-extractors`
        * a :class:`~scrapy.selector.Selector` object for a ``<link>`` or ``<a>`` element, e.g.
          ``response.css('a.my_link')[0]``
        * an attribute :class:`~scrapy.selector.Selector` (not SelectorList), e.g.
          ``response.css('a::attr(href)')[0]`` or
          ``response.xpath('//img/@src')[0]``

        See :ref:`response-follow-example` for usage examples.
        """
        ...
    
    def follow_all(self, urls=..., callback=..., method=..., headers=..., body=..., cookies=..., meta=..., encoding=..., priority=..., dont_filter=..., errback=..., cb_kwargs=..., flags=..., css=..., xpath=...) -> Generator[Request, None, None]:
        """
        A generator that produces :class:`~.Request` instances to follow all
        links in ``urls``. It accepts the same arguments as the :class:`~.Request`'s
        ``__init__`` method, except that each ``urls`` element does not need to be
        an absolute URL, it can be any of the following:

        * a relative URL
        * a :class:`~scrapy.link.Link` object, e.g. the result of
          :ref:`topics-link-extractors`
        * a :class:`~scrapy.selector.Selector` object for a ``<link>`` or ``<a>`` element, e.g.
          ``response.css('a.my_link')[0]``
        * an attribute :class:`~scrapy.selector.Selector` (not SelectorList), e.g.
          ``response.css('a::attr(href)')[0]`` or
          ``response.xpath('//img/@src')[0]``

        In addition, ``css`` and ``xpath`` arguments are accepted to perform the link extraction
        within the ``follow_all`` method (only one of ``urls``, ``css`` and ``xpath`` is accepted).

        Note that when passing a ``SelectorList`` as argument for the ``urls`` parameter or
        using the ``css`` or ``xpath`` parameters, this method will not produce requests for
        selectors from which links cannot be obtained (for instance, anchor tags without an
        ``href`` attribute)
        """
        ...
    


class _InvalidSelector(ValueError):
    """
    Raised when a URL cannot be obtained from a Selector
    """
    ...


