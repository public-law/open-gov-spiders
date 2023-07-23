from typing import cast

from scrapy.http.response.xml import XmlResponse

from public_law.test_util import *
from public_law.items.crs import Division, Article
from public_law.parsers.usa.colorado.crs import parse_title_bang


# Divisions aren't parsing correctly.
TITLE_1 =  XmlResponse(body = fixture('usa', 'crs', "title01.xml"), url = "title01.xml", encoding = "utf-8")
PARSED_TITLE_1 = parse_title_bang(TITLE_1, null_logger)

# A Title with no Divisions.
TITLE_4 =  XmlResponse(body = fixture('usa', 'crs', "title04.xml"), url = "title04.xml", encoding = "utf-8")
PARSED_TITLE_4 = parse_title_bang(TITLE_4, null_logger)

# A Title which uses Divisions.
TITLE_16 = XmlResponse(body = fixture('usa', 'crs', "title16.xml"), url = "title16.xml", encoding = "utf-8")
PARSED_TITLE_16 = parse_title_bang(TITLE_16, null_logger)


class TestParseErrors:
    def test_name(self):
        first_div = cast(Division, PARSED_TITLE_1.children[0])
        seventh_article = first_div.children[6]

        assert seventh_article.name == "Internet-based Voting Pilot Program for Absent Uniformed Services Electors"

    def test_title_number(self):
        first_div = cast(Division, PARSED_TITLE_1.children[0])
        seventh_article = first_div.children[6]

        assert seventh_article.title_number == "1"


class TestParseArticles:
    def test_correct_number_of_articles_in_a_division_1(self):
        # Title 16 contains eight Divisions.
        #   The first Division is _Code of Criminal Procedure_
        #       This Division contains 22 Articles.
        div_1_code_of_crim_pro = cast(Division, PARSED_TITLE_16.children[0])

        assert div_1_code_of_crim_pro.name          == "Code of Criminal Procedure"
        assert len(div_1_code_of_crim_pro.children) == 22


    def test_correct_number_of_articles_in_a_division_2(self):
        division_2 = cast(Division, PARSED_TITLE_16.children[1])
        
        assert division_2.name          == "Uniform Mandatory Disposition of Detainers Act"
        assert len(division_2.children) == 1


    def test_article_number_1(self):
        code_of_crim_pro = cast(Division, PARSED_TITLE_16.children[0])
        article_1        = code_of_crim_pro.children[0]

        assert article_1.number == "1"


    def test_article_name_1(self):
        div_1_code_of_crim_pro = cast(Division, PARSED_TITLE_16.children[0])
        article_1              = div_1_code_of_crim_pro.children[0]

        assert article_1.name == "General Provisions"


    def test_division_name_1(self):
        div_1_code_of_crim_pro = cast(Division, PARSED_TITLE_16.children[0])
        article_1              = div_1_code_of_crim_pro.children[0]

        assert article_1.division_name == "Code of Criminal Procedure"


class TestWithNoDivisions:
    def test_correct_count(self):
        """Title 4 contains 12 not-repealed Articles."""
        assert len(PARSED_TITLE_4.children) == 12

    def test_theyre_all_articles(self):
        for child in PARSED_TITLE_4.children:
            assert child.kind == "Article"


    ARTICLE_1 = cast(Article, PARSED_TITLE_4.children[0])

    def test_a_name(self):
        assert self.ARTICLE_1.name == "General Provisions"

    def test_a_number(self):
        assert self.ARTICLE_1.number == "1"

    def test_a_title_number(self):
        assert self.ARTICLE_1.title_number == "4"

    def test_a_division_name(self):
        assert self.ARTICLE_1.division_name is None


    ARTICLE_3 = cast(Article, PARSED_TITLE_4.children[2])

    def test_a_name_2(self):
        assert self.ARTICLE_3.name == "Leases"

    def test_a_number_2(self):
        assert self.ARTICLE_3.number == "2.5"

    def test_a_title_number_2(self):
        assert self.ARTICLE_3.title_number == "4"

    def test_a_division_name_2(self):
        assert self.ARTICLE_3.division_name is None


    # This should be the last article in Title 4.
    ARTICLE_9_7 = cast(Article, PARSED_TITLE_4.children[-1])

    def test_a_name_3(self):
        assert self.ARTICLE_9_7.name == "Colorado Statutory Lien Registration Act"

    def test_a_number_3(self):
        assert self.ARTICLE_9_7.number == "9.7"

    def test_a_title_number_3(self):
        assert self.ARTICLE_9_7.title_number == "4"
    
    def test_a_division_name_3(self):
        assert self.ARTICLE_9_7.division_name is None
