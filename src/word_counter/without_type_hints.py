def word_count(text):
    """Counts the number of words and chars in a text"""
    counts = {
        "words": {
            "total": len(text.split()),
            "unique": len(set(text.split())),
        },
        "chars": {
            "total": len(text),
            "unique": len(set(list(text))),
        },
    }
    return counts
