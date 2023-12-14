"""
This type stub file was generated by pyright.
"""

from scrapy.spiders import Spider

logger = ...
class SitemapSpider(Spider):
    sitemap_urls = ...
    sitemap_rules = ...
    sitemap_follow = ...
    sitemap_alternate_links = ...
    def __init__(self, *a, **kw) -> None:
        ...
    
    def start_requests(self): # -> Generator[Request, Any, None]:
        ...
    
    def sitemap_filter(self, entries): # -> Generator[Any, Any, None]:
        """This method can be used to filter sitemap entries by their
        attributes, for example, you can filter locs with lastmod greater
        than a given date (see docs).
        """
        ...
    


def regex(x): # -> Pattern[str]:
    ...

def iterloc(it, alt=...): # -> Generator[Any, Any, None]:
    ...

