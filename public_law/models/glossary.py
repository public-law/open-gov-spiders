from dataclasses import dataclass
import dataclasses
from functools import cache
from typing import Any, Iterable

from ..metadata import Metadata
from ..text import NonemptyString, Sentence
from ..nlp.flesch_reading_ease import Difficulty, reading_difficulty


@dataclass(frozen=True)
class GlossaryEntry:
    """Represents one term and its definition in a particular Glossary"""

    phrase: NonemptyString
    definition: Sentence

    def asdict(self):
        return dataclasses.asdict(self)


@dataclass(frozen=True)
class GlossaryParseResult:
    """All the info about a glossary"""

    metadata: Metadata
    entries: Iterable[GlossaryEntry]

    @cache
    def asdict(self):
        return {
            "metadata": self.metadata.asdict(),
            "entries": [entry.asdict() for entry in self.entries],
        }

    def __contains__(self, item: Any) -> bool:
        return self.asdict().__contains__(item)

    def __getitem__(self, item: Any) -> Any:
        return self.asdict().__getitem__(item)

    def __eq__(self, __t: Any):
        return self.asdict().__eq__(__t)

    def __ne__(self, __t: Any):
        return self.asdict().__ne__(__t)

    def __iter__(self):
        return self.asdict().__iter__()

    def __len__(self):
        return self.asdict().__len__()

    def __or__(self, __t: Any):
        return self.asdict().__or__(__t)

    def __ior__(self, __t: Any):
        return self.asdict().__ior__(__t)

    def __reversed__(self):
        return self.asdict().__reversed__()

    def __ror__(self, __t: Any):
        return self.asdict().__ror__(__t)

    def copy(self):
        return self.asdict().copy()

    def get(self, item: Any, default: Any = None):
        return self.asdict().get(item, default)

    def items(self):
        return self.asdict().items()

    def keys(self):
        return self.asdict().keys()

    def values(self):
        return self.asdict().values()


def reading_ease(entries: Iterable[GlossaryEntry]) -> Difficulty:
    """
    Calculate the readability level of a list of glossary entries.
    """
    return reading_difficulty(__definition_corpus(entries))


def __definition_corpus(entries: Iterable[GlossaryEntry]) -> NonemptyString:
    """
    All the definition text for this glossary.
    """
    return NonemptyString("  ".join(entry.definition for entry in entries))
