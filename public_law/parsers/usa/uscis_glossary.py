from typing import Any, Iterable

from more_itertools import chunked
from scrapy.http.response.html import HtmlResponse
from toolz.functoolz import pipe  # type: ignore

from ...flipped import lstrip, rstrip
from ...metadata import Metadata, Subject
from ...models.glossary import GlossaryEntry, GlossaryParseResult
from ...text import URL, LoCSubject, NonemptyString as String, WikidataTopic, make_soup
from ...text import (
    Sentence,
    capitalize_first_char,
    ensure_ends_with_period,
    normalize_nonempty,
)


def parse_glossary(html: HtmlResponse) -> GlossaryParseResult:
    """
    The top-level, public function of this module. It performs the
    complete parse of the HTTP response.
    """
    metadata = _make_metadata(html)
    entries  = _parse_entries(html)

    return GlossaryParseResult(metadata, entries)


def _make_metadata(html: HtmlResponse) -> Metadata:
    source_url = URL(html.url)  # type: ignore

    subjects = (
                Subject(LoCSubject("sh85042790"), String("Emigration and immigration law")),  # type: ignore
                Subject(WikidataTopic("Q231147"),  String("immigration law")),   # type: ignore
            )
    
    return Metadata(
            dcterms_title=String("USCIS Glossary"),
            dcterms_language="en",
            dcterms_coverage="USA",
            # Info about original source
            dcterms_source=source_url,
            publiclaw_sourceModified="unknown",
            publiclaw_sourceCreator=String("The Courts Service of Ireland"),
            dcterms_subject=subjects,
        )


def _parse_entries(html: HtmlResponse) -> Iterable[GlossaryEntry]:
    """
    TODO: Refactor into a parent class. Write a way to pass lists of
    functions for cleaning up the definitions and phrases.
    """

    def cleanup_definition(defn: str) -> Sentence:
        return pipe(
            defn,
            normalize_nonempty,
            lstrip(":"),  # type: ignore
            ensure_ends_with_period,
            normalize_nonempty,
            capitalize_first_char,
            Sentence,
        )

    def cleanup_phrase(phrase: str) -> String:
        return pipe(
            phrase,
            rstrip(":"),  # type: ignore
            normalize_nonempty,
            String,
        )

    for phrase, defn in _raw_entries(html):
        yield GlossaryEntry(
            phrase=cleanup_phrase(phrase),
            definition=cleanup_definition(defn),
        )


def _raw_entries(html: HtmlResponse) -> Iterable[tuple[Any, Any]]:
    """
    The core of this parser.

    TODO: Refactor all the glossary parsers to need only this function.
    """

    soup      = make_soup(html)
    phrases   = [d.string for d in soup.select('div.accordion__header')]  # type: ignore

    defn_divs = [list(d.children) for d in soup.select('div.accordion__panel')]  # type: ignore
    cleaned_up_definitions = []
    for div in defn_divs:
        cleaned_up = "\n".join([str(s) for s in div if str(s) != '\n'])
        cleaned_up_definitions.append(cleaned_up)  # type: ignore


    return zip(phrases, cleaned_up_definitions)
