from dataclasses import dataclass, asdict

from public_law.dates import todays_date
from public_law.text import NonemptyString


@dataclass(frozen=True)
class Metadata:
    """Each JSON output file should have a `Metadata` object with the attributes:

    - `dc:creator`
    - `dc:identifier`
    - `dc:language`
    - `dc:publisher`
    - `dc:source`
    - `dc:type`
    - `dc:title`
    - `dcterms:license`
    - `dcterms:modified`

    See:

    * [Publishing Metadata](https://www.dublincore.org/resources/userguide/publishing_metadata/)
    * [Creating Metadata](https://www.dublincore.org/resources/userguide/creating_metadata/)
    * [Dublin Core Specifications](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)
    """

    dc_title: NonemptyString
    dc_language: NonemptyString
    dc_source: NonemptyString
    dc_identifier: NonemptyString
    dc_creator: NonemptyString

    dc_publisher: str = "Public.Law"
    dc_type: str = "text"
    dcterms_license: str = "https://creativecommons.org/licenses/by/4.0/"
    dcterms_modified: str = todays_date()

    def as_dict(self) -> dict:
        """Return a dict containing the metadata with proper DublinCore
        naming syntax. Instead of keys such as `dc_title`, they should be
        in the form, `dc:title`."""

        new_dict = {}
        for old_key, value in asdict(self).items():
            new_key = old_key.replace("_", ":")
            new_dict[new_key] = value

        return new_dict
