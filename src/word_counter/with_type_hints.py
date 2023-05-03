from pydantic import BaseModel


class Counts(BaseModel):
    total: int
    unique: int


class CountResults(BaseModel):
    words: Counts
    chars: Counts


def word_count(text: str) -> CountResults:
    """Counts the number of words and chars in a text"""
    word_counts = Counts(
        total=len(text.split()),
        unique=len(set(text.split())),
    )
    char_counts = Counts(
        total=len(text),
        unique=len(set(list(text))),
    )
    return CountResults(words=word_counts, chars=char_counts)
