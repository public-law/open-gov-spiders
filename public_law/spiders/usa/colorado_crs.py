import os
from pathlib import Path

from scrapy import Spider
from scrapy.http.request import Request
from scrapy.http.response.html import HtmlResponse
from typing import Any

from public_law.parsers.usa.colorado.crs import parse_title


class ColoradoCRS(Spider):
    """Spider for the Colorado CRS XML files.

    Reads the sources from a local directory instead of the web.
    """
    name = "usa_colorado_crs"
    XML_DIR  = f"{os.getcwd()}/tmp/sources/CRSDATA20220915/TITLES"

    def start_requests(self):
        for path in sorted(Path(self.XML_DIR).glob("*.xml")):
            yield Request(url=f"file://{path}", callback=self.parse)


    def parse(self, response: HtmlResponse, **_: dict[str, Any]):
        """Framework callback which begins the parsing."""
        print(f"response.url: {response.url}")
        yield parse_title(response)
