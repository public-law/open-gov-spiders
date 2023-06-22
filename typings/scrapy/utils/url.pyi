"""
This type stub file was generated by pyright.
"""

from w3lib.url import *

"""
This module contains general purpose URL functions not found in the standard
library.

Some of the functions that used to be imported from this module have been moved
to the w3lib.url module. Always import those from there instead.
"""
def url_is_from_any_domain(url, domains): # -> bool:
    """Return True if the url belongs to any of the given domains"""
    ...

def url_is_from_spider(url, spider): # -> bool:
    """Return True if the url belongs to the given spider"""
    ...

def url_has_any_extension(url, extensions): # -> bool:
    """Return True if the url ends with one of the extensions provided"""
    ...

def parse_url(url, encoding=...): # -> ParseResult:
    """Return urlparsed url from the given argument (which could be an already
    parsed url)
    """
    ...

def escape_ajax(url): # -> str:
    """
    Return the crawleable url according to:
    https://developers.google.com/webmasters/ajax-crawling/docs/getting-started

    >>> escape_ajax("www.example.com/ajax.html#!key=value")
    'www.example.com/ajax.html?_escaped_fragment_=key%3Dvalue'
    >>> escape_ajax("www.example.com/ajax.html?k1=v1&k2=v2#!key=value")
    'www.example.com/ajax.html?k1=v1&k2=v2&_escaped_fragment_=key%3Dvalue'
    >>> escape_ajax("www.example.com/ajax.html?#!key=value")
    'www.example.com/ajax.html?_escaped_fragment_=key%3Dvalue'
    >>> escape_ajax("www.example.com/ajax.html#!")
    'www.example.com/ajax.html?_escaped_fragment_='

    URLs that are not "AJAX crawlable" (according to Google) returned as-is:

    >>> escape_ajax("www.example.com/ajax.html#key=value")
    'www.example.com/ajax.html#key=value'
    >>> escape_ajax("www.example.com/ajax.html#")
    'www.example.com/ajax.html#'
    >>> escape_ajax("www.example.com/ajax.html")
    'www.example.com/ajax.html'
    """
    ...

def add_http_if_no_scheme(url):
    """Add http as the default scheme if it is missing from the url."""
    ...

def guess_scheme(url): # -> str:
    """Add an URL scheme if missing: file:// for filepath-like input or
    http:// otherwise."""
    ...

def strip_url(url, strip_credentials=..., strip_default_port=..., origin_only=..., strip_fragment=...): # -> str:
    """Strip URL string from some of its components:

    - ``strip_credentials`` removes "user:password@"
    - ``strip_default_port`` removes ":80" (resp. ":443", ":21")
      from http:// (resp. https://, ftp://) URLs
    - ``origin_only`` replaces path component with "/", also dropping
      query and fragment components ; it also strips credentials
    - ``strip_fragment`` drops any #fragment component
    """
    ...

