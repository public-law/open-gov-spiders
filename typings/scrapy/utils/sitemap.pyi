"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

"""
Module for processing Sitemaps.

Note: The main purpose of this module is to provide support for the
SitemapSpider, its API is subject to change without notice.
"""
class Sitemap(object):
    """Class to parse Sitemap (type=urlset) and Sitemap Index
    (type=sitemapindex) files"""
    def __init__(self, xmltext):
        self.type = ...
    
    def __iter__(self):
        ...
    


def sitemap_urls_from_robots(robots_text, base_url: Optional[Any] = ...):
    """Return an iterator over all sitemap urls contained in the given
    robots.txt file
    """
    ...

