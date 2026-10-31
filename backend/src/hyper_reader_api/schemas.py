"""HTTP contract of the API."""

from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

LanguageTag = Annotated[str, Field(min_length=2, max_length=35)]
"""A BCP 47 language tag, e.g. `en`, `es`, `pt-BR`."""


class ApiModel(BaseModel):
    """Base for HTTP payloads: camelCase on the wire, snake_case in Python."""

    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True)


class TranslationRequest(ApiModel):
    book_language: LanguageTag
    """Language of the book."""

    target_language: LanguageTag
    """Reader's native language, which the translation and note are written in."""

    word: str = Field(min_length=1, max_length=200)
    """The tapped word, or the text of a multi-word token range."""

    sentence: str = Field(min_length=1, max_length=2000)
    """The sentence the word appears in, used to pick the right sense."""


class TranslationResult(ApiModel):
    translation: str
    """Translation of the word in context, in the target language."""

    lemma: str
    """Dictionary form of the word, in the book language."""

    note: str
    """Short explanation, in the target language."""
