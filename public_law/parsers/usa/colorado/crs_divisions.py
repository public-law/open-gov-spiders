# pyright: reportUnknownMemberType=false
# pyright: reportOptionalMemberAccess=false
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnknownLambdaType=false


from scrapy.selector.unified import Selector
from scrapy.http.response import Response

from typing import Any
from itertools import takewhile, dropwhile


from public_law.selector_util import just_text
from public_law.text import NonemptyString
from public_law.items.crs import Division, Subdivision
from public_law.parsers.usa.colorado.crs_articles import div_name_text, parse_articles_from_division



def parse_divisions(title_number: NonemptyString, dom: Selector | Response, logger: Any) -> list[Division]:
    division_nodes = dom.xpath("//T-DIV")

    divs = []
    for div_node in division_nodes:
        raw_div_name = div_name_text(div_node)
        print(f"Raw div name: {raw_div_name}")

        if raw_div_name is None:
            logger.warn(f"Could not parse division name in {div_node.get()}, Title {title_number}")
            continue

        try:
            if _has_subdivisions(dom):
                if Division.is_valid_raw_name(raw_div_name):
                    subdivisions = parse_subdivisions_from_division(title_number, dom, raw_div_name)
                    if len(subdivisions) > 0:
                        divs.append(
                            Division(
                                raw_name     = raw_div_name,
                                children     = subdivisions,
                                title_number = title_number
                                )
                            )
                    else:
                        divs.append(
                            Division(
                                raw_name     = raw_div_name,
                                children     = parse_articles_from_division(title_number, dom, raw_div_name),
                                title_number = title_number
                                )
                            )
            else:
                divs.append(
                    Division(
                        raw_name     = raw_div_name,
                        children     = parse_articles_from_division(title_number, dom, raw_div_name),
                        title_number = title_number
                        )
                    )
        except ValueError:
            logger.warn(f"Could not parse division name in {raw_div_name}, Title {title_number}")

    return divs


def parse_subdivisions_from_division(title_number: NonemptyString, dom: Selector | Response, raw_div_name: str) -> list[Subdivision]:
    """Return the Subdivisions within the given Division."""

    print(f"parse_subdivisions_from_division() with: {raw_div_name}")

    #
    # Algorithm:
    #
    # 1. Get all the Divs and Subdivs.
    divs_and_subdivs = dom.xpath("//TITLE-ANAL/T-DIV")

    # 2. Find the T-DIV with the Division name.
    partial_list = list(dropwhile(
        lambda n: div_name_text(n) != raw_div_name, 
        divs_and_subdivs
        ))

    if len(partial_list) == 0:
        print("No partial list\n")
        return []

    # 3. `takewhile` all the following T-DIV elements
    #    and stop at the end of the Subdivs.
    _head = partial_list[0]
    tail  = partial_list[1:]
    subdiv_nodes = takewhile(_is_subdiv_node, tail)

    # 4. Convert the T-DIV elements into Subdivisions.
    return [
        Subdivision(
            raw_name = NonemptyString(just_text(n)),
            articles = parse_articles_from_division(title_number, dom, raw_div_name, Subdivision.name_from_raw(NonemptyString(just_text(n)))),
            title_number = title_number,
            division_name = Division.name_from_raw(raw_div_name)
            )
        for n in subdiv_nodes
        ]


def _is_subdiv_node(node: Selector) -> bool:
    return Subdivision.is_valid_raw_name(just_text(node))


def _has_subdivisions(dom: Selector | Response) -> bool:
    raw_div_names = [just_text(e) for e in dom.xpath("//TITLE-ANAL/T-DIV")]
    
    return not all([Division.is_valid_raw_name(n) for n in raw_div_names])
