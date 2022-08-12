from more_itertools import first, last
from public_law.dates import today
from public_law.metadata import Subject
from public_law.models.glossary import GlossaryParseResult
from public_law.parsers.aus.ip_glossary import parse_glossary
from public_law.text import URL, NonemptyString
from scrapy.http.response.html import HtmlResponse


def parsed_fixture(filename: str, url: str) -> GlossaryParseResult:
    with open(f"tests/fixtures/aus/{filename}", encoding="utf8") as f:
        html = HtmlResponse(
            url=url,
            body=f.read(),
            encoding="UTF-8",
        )

    return parse_glossary(html)


PARSED_GLOSSARY_FIXTURE = parsed_fixture(
    filename="ip-glossary.html",
    url="https://www.ipaustralia.gov.au/tools-resources/ip-glossary",
)


def test_the_name():
    assert PARSED_GLOSSARY_FIXTURE.metadata.dcterms_title == "IP Glossary"


def test_url():
    assert (
        PARSED_GLOSSARY_FIXTURE.metadata.dcterms_source
        == "https://www.ipaustralia.gov.au/tools-resources/ip-glossary"
    )


# def test_author():
#     assert PARSED_GLOSSARY_FIXTURE.metadata.dcterms_creator == "https://public.law"


# def test_coverage():
#     assert PARSED_GLOSSARY_FIXTURE.metadata.dcterms_coverage == "NZL"


# def test_source_modified_date():
#     assert PARSED_GLOSSARY_FIXTURE.metadata.publiclaw_sourceModified == "unknown"


# def test_scrape_date():
#     assert PARSED_GLOSSARY_FIXTURE.metadata.dcterms_modified == today()


# def test_phrase():
#     assert first(PARSED_GLOSSARY_FIXTURE.entries).phrase == "acquit"


# def test_definition():
#     assert (
#         first(PARSED_GLOSSARY_FIXTURE.entries).definition
#         == "To decide officially in court that a person is not guilty."
#     )


# def test_proper_number_of_entries():
#     assert len(tuple(PARSED_GLOSSARY_FIXTURE.entries)) == 154


# def test_last_entry():
#     last_entry = last(PARSED_GLOSSARY_FIXTURE.entries)

#     assert last_entry.phrase == "Youth Court"
#     assert last_entry.definition == (
#         "The Youth Court has jurisdiction to deal with "
#         "young people charged with criminal offences."
#     )


# def test_reading_ease():
#     assert PARSED_GLOSSARY_FIXTURE.metadata.publiclaw_readingEase == "Fairly difficult"


# def test_subjects():
#     assert PARSED_GLOSSARY_FIXTURE.metadata.dcterms_subject == (
#         Subject(
#             uri=URL("http://id.loc.gov/authorities/subjects/sh85071120"),
#             rdfs_label=NonemptyString("Justice, Administration of"),
#         ),
#         Subject(
#             uri=URL("https://www.wikidata.org/wiki/Q16514399"),
#             rdfs_label=NonemptyString("Administration of justice"),
#         ),
#     )
