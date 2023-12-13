from typing import Any, Dict, List, cast

from scrapy import Spider
from scrapy.selector.unified import Selector
from scrapy.crawler import Crawler
import scrapy.exceptions
from scrapy.http.response import Response
from scrapy.http.request import Request
import scrapy.signals

from public_law.items.oar import Chapter, Division, OAR
from public_law.parsers.usa.oregon_regs import DOMAIN, oar_url, parse_division
from public_law.dates import todays_date
from public_law.text  import titleize


JD_VERBOSE_NAME = "USA / Oregon"
PUBLICATION_NAME = "Oregon Administrative Rules"


class OregonRegs(Spider):
    name = "usa_or_regs"
    allowed_domains = [DOMAIN]
    start_urls = [oar_url("ruleSearch.action")]

    def __init__(self, *args: List[str], **kwargs: Dict[str, Any]):
        super().__init__(*args, **kwargs)  # type: ignore

        # A flag, set after post-processing is finished, to avoid an infinite
        # loop.
        self.data_submitted = False

        # The object to return for conversion to a JSON tree. All the parse
        # methods add their results to this structure.
        self.oar = OAR(date_accessed=todays_date(), chapters=[])

    def parse(self, response: Response, **_kwargs: Dict[str, Any]):
        """The primary Scrapy callback to begin scraping.

        Kick off scraping by parsing the main OAR page.
        """
        return self.parse_search_page(response)

    def parse_search_page(self, response: Response):
        """Parse the top-level page.

        The search page contains a list of Chapters, with the names,
        numbers, and internal id's.
        """
        for option in response.css("#browseForm option"):  # type: ignore
            db_id: Any = option.xpath("@value").get()  # type: ignore
            if db_id == "-1":  # Ignore the heading
                continue

            number, name = map(str.strip, option.xpath("text()").get().split("-", 1)) # pyright: ignore[reportUnknownArgumentType, reportUnknownMemberType]
            chapter = new_chapter(db_id, number, name)

            new_chapter_index = len(self.oar["chapters"])  # type: ignore
            self.oar["chapters"].append(chapter)  # type: ignore

            request = Request(chapter["url"], callback=self.parse_chapter_page) # pyright: ignore[reportUnknownArgumentType]
            request.meta["chapter_index"] = new_chapter_index  # type: ignore
            yield request

    def parse_chapter_page(self, response: Response):
        """Parse a mid-level page.

        A Chapter's page contains a hierarchical list of all its Divisions
        along with their contained Rules.
        """
        chapter: Chapter = cast(Chapter, self.oar["chapters"][response.meta["chapter_index"]]) # pyright: ignore[reportUnknownMemberType]

        # Collect the Divisions
        anchor: Selector
        for anchor in response.css("#accordion > h3 > a"):  # type: ignore
            db_id: str = cast(str, anchor.xpath("@href").get().split("selectedDivision=")[1]) # pyright: ignore[reportUnknownMemberType, reportOptionalMemberAccess]
            raw_number, raw_name = map(
                str.strip, anchor.xpath("text()").get().split("-", 1) # pyright: ignore[reportUnknownArgumentType, reportUnknownMemberType, reportOptionalMemberAccess]
            )
            number: str = raw_number.split(" ")[1]
            name: str = titleize(raw_name)
            division = new_division(db_id, number, name)

            chapter["divisions"].append(division) # pyright: ignore[reportUnknownMemberType]

            # Request a scrape of the Division page
            request = Request(division["url"], callback=self.parse_division_page)  # type: ignore
            request.meta["division_index"] = len(chapter["divisions"]) - 1  # type: ignore
            request.meta["chapter_index"] = response.meta["chapter_index"]  # type: ignore
            yield request

    def parse_division_page(self, response: Response):
        chapter: Chapter = self.oar["chapters"][response.meta["chapter_index"]]  # type: ignore
        division: Division = chapter["divisions"][response.meta["division_index"]]  # type: ignore

        division["rules"].extend(parse_division(response))  # type: ignore

    #
    # Output a single object: a JSON tree containing all the scraped data. This
    # code implements that strategy by registering a signal event listener to
    # execute after all scraping has finished and the data is collected.
    #

    @classmethod
    def from_crawler(cls, crawler: Crawler, *args: List[str], **kwargs: Dict[str, Any]):
        """Override to register to receive the idle event"""
        spider = cast(OregonRegs, super(OregonRegs, cls).from_crawler(crawler, *args, **kwargs))

        crawler.signals.connect(spider.spider_idle, signal=scrapy.signals.spider_idle)  # type: ignore
        return spider

    def spider_idle(self, spider: Spider):
        """Schedule a simple request to return the collected data"""
        if self.data_submitted:
            return

        # This is a hack: I don't yet know how to schedule a request to just
        # submit data _without_ also triggering a scrape. So I provide a URL
        # to a simple site that we're going to ignore.
        null_request = Request(
            "https://www.public.law/about-us", callback=self.submit_data  # type: ignore
        )
        self.crawler.engine.schedule(null_request, spider)  # type: ignore
        raise scrapy.exceptions.DontCloseSpider

    def submit_data(self, _):
        """Simply return the collection of all the scraped data.

        Ignore the actual scraped content. I haven't figured out another
        way to submit the merged results. To be used as a callback when
        the spider is idle (i.e., has finished scraping.)
        """
        self.data_submitted = True
        yield self.oar


def new_chapter(db_id: str, number: str, name: str) -> Chapter:
    return Chapter(
        kind="Chapter",
        db_id=db_id,
        number=number,
        name=name,
        url=oar_url(f"displayChapterRules.action?selectedChapter={db_id}"),
        divisions=[],
    )


def new_division(db_id: str, number: str, name: str) -> Division:
    return Division(
        kind="Division",
        db_id=db_id,
        number=number,
        name=name,
        url=oar_url(f"displayDivisionRules.action?selectedDivision={db_id}"),
        rules=[],
    )
