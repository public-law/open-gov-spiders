import re
from typing import Any, Dict

from public_law.parsers.int.rome_statute import articles, footnotes, new_metadata, parts
from scrapy import Spider
from scrapy.http.response import Response


class RomeStatute(Spider):
    name = "rome_statute"
    start_urls = [
        "https://www.icc-cpi.int/resource-library",
    ]

    def parse(self, response: Response, **_kwargs: Dict[str, Any]):
        """Scrapy framework callback which begins the parsing."""

        for url in start_page_urls(response):
            if "Rome-Statute.pdf" not in url:  # Skip non-English versions for now.
                continue

            yield {"metadata": new_metadata(url).as_dublin_core_dict()}

            for part in parts(url):
                yield {"part": part.dict()}

            for article in articles(url):
                yield {"article": article.dict()}

            for footnote in footnotes():
                yield {"footnote": footnote.dict()}


#
# Pure helper functions
#


def start_page_urls(response: Response) -> list[str]:
    anchors = response.css("h2#coreICCtexts + p + div").css("a").getall()[:4]  # type: ignore
    relative_urls = [re.findall(r'"(.+)"', a)[0] for a in anchors]  # type: ignore
    absolute_urls = ["https://www.icc-cpi.int" + url for url in relative_urls]

    return absolute_urls
