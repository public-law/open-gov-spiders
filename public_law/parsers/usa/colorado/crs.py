# pyright: reportUnknownMemberType=false
# pyright: reportOptionalMemberAccess=false
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnknownLambdaType=false
# pyright: reportGeneralTypeIssues=false


from scrapy.selector.unified import Selector
from titlecase import titlecase
from itertools import takewhile, dropwhile
from typing import cast
from public_law.text import remove_trailing_period

from public_law.items.crs import Article, Division, Title


def parse_title(dom: Selector) -> Title:
    print(f"{dom=}")
    raw_name   = cast(str, dom.xpath("//title-text/text()").get())
    raw_number = dom.xpath("//title-num/text()").get().split(" ")[1]

    url_number = raw_number.rjust(2, "0")
    source_url = f"https://leg.colorado.gov/sites/default/files/images/olls/crs2021-title-{url_number}.pdf"

    return Title(
        name=titlecase(raw_name),
        number=raw_number,
        divisions=_parse_divisions(dom, source_url),
        source_url=source_url,
    )


def _parse_divisions(dom: Selector, source_url: str) -> list[Division]:
    raw_division_names = dom.xpath("//t-div/text()")

    return [
        Division(
            name=titlecase(div_node.get()),
            source_url=source_url,
            articles=_parse_articles(dom, div_node, titlecase(div_node.get()), source_url),
        )
        for div_node in raw_division_names
    ]


def _parse_articles(dom: Selector, div_node: Selector, name: str, source_url: str) -> list[Article]:
    """Return the articles within the given Division."""

    #
    # Algorithm:
    #
    # 1. Get all the child elements of TITLE-ANAL.
    divs_and_articles = dom.xpath("//title-anal/t-div | //title-anal/ta-list")

    # 2. Find the T-DIV with the Division name.
    partial_list = list(dropwhile(
        lambda n: titlecase(n.xpath("text()").get()) != name, 
        divs_and_articles
        ))

    # 3. `takewhile` all the following TA-LIST elements
    #    and stop at the end of the Articles.
    _head = partial_list[0]
    tail = partial_list[1:]
    article_nodes = takewhile(is_article_node, tail)

    # 4. Convert the TA-LIST elements into Article objects.    
    articles = [
        Article(
            name=parse_article_name(n), 
            number=parse_article_number(n), 
            source_url=source_url
            ) 
        for n in article_nodes
        ]

    return articles


def is_article_node(node: Selector):
    return node_name(node) == "ta-list"

def node_name(node: Selector):
    return node.xpath("name()").get()


def parse_article_name(node: Selector):
    """Return just the name of the Article.
    The raw text looks like this:
        "General, Provisions, 16-1-101 to 16-1-110"
    
    We want to return just the first part:
        "General, Provisions"
    """
    raw_text     = node.xpath("i/text()").get()
    cleaned_text = ", ".join(raw_text.split(",")[:-1])

    return cleaned_text

def parse_article_number(node: Selector):
    """Return just the number of the Article.
    The raw text looks like this:
        "1.1."
    
    We want to return just this:
        "1.1"
    """
    raw_text     = node.xpath("dt/text()").get()
    cleaned_text = remove_trailing_period(raw_text)

    return cleaned_text
