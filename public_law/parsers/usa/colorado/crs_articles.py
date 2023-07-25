# pyright: reportUnknownMemberType=false
# pyright: reportOptionalMemberAccess=false
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnknownLambdaType=false

from itertools import takewhile, dropwhile
from typing import Any

from bs4 import BeautifulSoup

from scrapy.selector.unified import Selector
from scrapy.http.response import Response

from public_law.selector_util import node_name
from public_law.items.crs import Article, Division
from public_law.text import remove_trailing_period, normalize_whitespace, NonemptyString


def parse_articles_from_division(
        title_number: NonemptyString, 
        dom: Selector | Response, 
        raw_div_name: str, 
        subdiv_name: NonemptyString|None = None) -> list[Article]:
    """Return the articles within the given Division."""

    #
    # Algorithm:
    #
    # 1. Get all the child elements of TITLE-ANAL.
    divs_and_articles = dom.xpath("//TITLE-ANAL/T-DIV | //TITLE-ANAL/TA-LIST")

    # 2. Find the T-DIV with the Division or Subdivision name.
    if subdiv_name is not None:
        search_string = subdiv_name
    else:
        search_string = raw_div_name

    partial_list = list(dropwhile(
        lambda n: div_name_text(n) != search_string, 
        divs_and_articles
        ))

    if len(partial_list) == 0:
        return []

    # 3. `takewhile` all the following TA-LIST elements
    #    and stop at the end of the Articles.
    _head = partial_list[0]
    tail  = partial_list[1:]
    article_nodes = takewhile(_is_article_node, tail)

    # 4. Convert the TA-LIST elements into Article objects.   
    return [
        Article(
            name =   _parse_article_name(n), 
            number = _parse_article_number(n),
            title_number = title_number,
            division_name= Division.name_from_raw(raw_div_name),
            subdivision_name= subdiv_name,
            ) 
        for n in article_nodes
        ]



def parse_articles(title_number: NonemptyString, dom: Selector | Response, logger: Any) -> list[Article]:
    #
    # Algorithm:
    #
    # 1. Get all the child elements of TITLE-ANAL.
    articles = dom.xpath("//TITLE-ANAL/TA-LIST")

    if len(articles) == 0:
        logger.warn(f"Could not parse articles in Title {title_number}")
        return []

    # 3. `takewhile` all the following TA-LIST elements
    #    and stop at the end of the Articles.
    article_nodes = takewhile(_is_article_node, articles)

    # 4. Convert the TA-LIST elements into Article objects.   
    return [
        Article(
            name             = _parse_article_name(n), 
            number           = _parse_article_number(n),
            title_number     = title_number,
            division_name    = None,
            subdivision_name = None,
            ) 
        for n in article_nodes
        ]



def _is_article_node(node: Selector) -> bool:
    return node_name(node) == "TA-LIST"


def _parse_article_name(node: Selector) -> NonemptyString:
    """Return just the name of the Article.
    The raw text looks like this:
        "General, Provisions, 16-1-101 to 16-1-110"
    
    We want to return just the first part:
        "General, Provisions"
    """
    match node.xpath("I/text()").get():
        case str(text):
            raw_text     = normalize_whitespace(text)
            cleaned_text = ", ".join(raw_text.split(",")[:-1])
            if cleaned_text == "":
                cleaned_text = raw_text
            return NonemptyString(cleaned_text)
        case None:
            raise Exception("Could not parse article name in {node}")


def _parse_article_number(node: Selector) -> NonemptyString:
    """Return just the number of the Article.
    The raw text looks like this:
        "1.1."
    
    We want to return just this:
        "1.1"
    """
    match node.xpath("DT/text()").get():
        case str(raw_text):
            return NonemptyString(remove_trailing_period(raw_text))
        case None:
            raise Exception("Could not parse article number in {node}")


def div_name_text(div_node: Selector) -> NonemptyString | None:
    soup = BeautifulSoup(div_node.get(), 'xml')
    soup_text = soup.get_text()
    cleaned_up_text = normalize_whitespace(soup_text)
    try:
        return NonemptyString(cleaned_up_text)
    except ValueError:
        return None
