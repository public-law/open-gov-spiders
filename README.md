[![Test Suite](https://github.com/public-law/open-gov-crawlers/actions/workflows/python-app.yml/badge.svg)](https://github.com/public-law/open-gov-crawlers/actions/workflows/python-app.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/3978810b3733b415a266/maintainability)](https://codeclimate.com/github/public-law/open-gov-crawlers/maintainability)


# Open-gov spiders written in Python

| Jurisdiction | Publication | Source code | Dataset |
| :----------- | :---------- | :---------- | :------ |
| Canada | Dept. of Justice Legal Glossaries | [parser](https://github.com/public-law/open-gov-crawlers/blob/master/public_law/parsers/usa/georgia_ag_opinions.py), [spider](https://github.com/public-law/open-gov-crawlers/blob/master/public_law/spiders/usa/georgia_ag_opinions.py), [tests](https://github.com/public-law/open-gov-crawlers/blob/master/tests/public_law/parsers/usa/georgia_ag_opinionstest.py) | [json](https://github.com/public-law/datasets/blob/master/Canada/doj-glossaries.json) |
| Intergovernmental | Rome Statute | [parser](https://github.com/public-law/open-gov-crawlers/blob/master/public_law/parsers/usa/georgia_ag_opinions.py), [spider](https://github.com/public-law/open-gov-crawlers/blob/master/public_law/spiders/usa/georgia_ag_opinions.py), [tests](https://github.com/public-law/open-gov-crawlers/blob/master/tests/public_law/parsers/usa/georgia_ag_opinionstest.py) | [json](https://github.com/public-law/datasets/blob/master/Intergovernmental/RomeStatute/RomeStatute.json) |
| Ireland | Glossary of Legal Terms | [parser](https://github.com/public-law/open-gov-crawlers/blob/master/public_law/parsers/usa/georgia_ag_opinions.py), [spider](https://github.com/public-law/open-gov-crawlers/blob/master/public_law/spiders/usa/georgia_ag_opinions.py), [tests](https://github.com/public-law/open-gov-crawlers/blob/master/tests/public_law/parsers/usa/georgia_ag_opinionstest.py) | [json](https://github.com/public-law/datasets/blob/master/Ireland/courts-glossary.json) |
| New Zealand | Glossary | [parser](https://github.com/public-law/open-gov-crawlers/blob/master/public_law/parsers/usa/georgia_ag_opinions.py), [spider](https://github.com/public-law/open-gov-crawlers/blob/master/public_law/spiders/usa/georgia_ag_opinions.py), [tests](https://github.com/public-law/open-gov-crawlers/blob/master/tests/public_law/parsers/usa/georgia_ag_opinionstest.py) | [json](https://github.com/public-law/datasets/blob/master/NewZealand/justice-glossary.json) |
| USA | US Courts Glossary | [parser](https://github.com/public-law/open-gov-crawlers/blob/master/public_law/parsers/usa/georgia_ag_opinions.py), [spider](https://github.com/public-law/open-gov-crawlers/blob/master/public_law/spiders/usa/georgia_ag_opinions.py), [tests](https://github.com/public-law/open-gov-crawlers/blob/master/tests/public_law/parsers/usa/georgia_ag_opinionstest.py) | [json](https://github.com/public-law/datasets/blob/master/UnitedStates/us-courts-glossary.json) |
| USA / Georgia | Attorney General Opinions | [parser](https://github.com/public-law/open-gov-crawlers/blob/master/public_law/parsers/usa/georgia_ag_opinions.py), [spider](https://github.com/public-law/open-gov-crawlers/blob/master/public_law/spiders/usa/georgia_ag_opinions.py), [tests](https://github.com/public-law/open-gov-crawlers/blob/master/tests/public_law/parsers/usa/georgia_ag_opinionstest.py) |  |
| USA / Oregon | Oregon Administrative Rules | [parser](https://github.com/public-law/open-gov-crawlers/blob/master/public_law/parsers/usa/georgia_ag_opinions.py), [spider](https://github.com/public-law/open-gov-crawlers/blob/master/public_law/spiders/usa/georgia_ag_opinions.py), [tests](https://github.com/public-law/open-gov-crawlers/blob/master/tests/public_law/parsers/usa/georgia_ag_opinionstest.py) |  |


> FYI: We're looking for paid help writing more spiders like these, especially in languages other than English. [See the wiki](https://github.com/public-law/open-gov-crawlers/wiki) for a technical explanation
> of our parsing strategy. And check out the links, above, for our coding style.


## Example: Oregon Administrative Rules Parser
The spiders retrieve the HTML pages and output well formed JSON which represents the source's structure.
First, we can see which spiders are available:

```bash
$ scrapy list

can_doj_glossaries
int_rome_statute
irl_courts_glossary
nzl_justice_glossary
usa_courts_glossary
usa_ga_attorney_general_opinions
usa_or_regs
```

Then we can run one of the spiders:

```bash
$ scrapy crawl usa_or_regs
```

This produces the output:

```json
{
  "date_accessed": "2019-03-21",
  "chapters": [
    {
      "kind": "Chapter",
      "db_id": "36",
      "number": "101",
      "name": "Oregon Health Authority, Public Employees' Benefit Board",
      "url": "https://secure.sos.state.or.us/oard/displayChapterRules.action?selectedChapter=36",
      "divisions": [
        {
          "kind": "Division",
          "db_id": "1",
          "number": "1",
          "name": "Procedural Rules",
          "url": "https://secure.sos.state.or.us/oard/displayDivisionRules.action?selectedDivision=1",
          "rules": [
            {
              "kind": "Rule",
              "number": "101-001-0000",
              "name": "Notice of Proposed Rule Changes",
              "url": "https://secure.sos.state.or.us/oard/view.action?ruleNumber=101-001-0000",
              "authority": [
                "ORS 243.061 - 243.302"
              ],
              "implements": [
                "ORS 183.310 - 183.550",
                "192.660",
                "243.061 - 243.302",
                "292.05"
              ],
              "history": "PEBB 2-2009, f. 7-29-09, cert. ef. 8-1-09<br>PEBB 1-2009(Temp), f. &amp; cert. ef. 2-24-09 thru 8-22-09<br>PEBB 1-2004, f. &amp; cert. ef. 7-2-04<br>PEBB 1-1999, f. 12-8-99, cert. ef. 1-1-00",
              }
            ]
          }
        ]
      }
    ]
  }
```
(etc.)

[The Wiki](https://github.com/public-law/open-gov-crawlers/wiki) explains the JSON strategy.


Development Environment Notes
-----------------------------

### Python 3.10.5

I'm using [asdf](https://asdf-vm.com/#/) because the Homebrew distribution
is more up-to-date than pyenv.


### [Poetry](https://python-poetry.org/) for dependency management

So before I start working, I go into the virtual environment:

```bash
poetry shell
```

Making sure I have the current deps installed is always good to do:

```bash
poetry install
```

### Pytest for testing

The pytest tests run easily:

```bash
pytest
```

## Other tools

* Java is required by the Python Tika package.
* Pylance/Pyright for type-checking
* Black for formatting


### Dependencies; helpful links

* [The Scrapy Playbook](https://thepythonscrapyplaybook.com)
* [The Zyte runtime environments](https://github.com/scrapinghub/scrapinghub-stack-scrapy/tags)
* [SHUB Configuration](https://shub.readthedocs.io/en/stable/configuration.html)
