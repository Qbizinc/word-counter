from word_counter.without_type_hints import word_count


def test_total_counts_matches_unique_counts():
    """Total and unique counts should match when all words and chars are unique"""
    # setup
    expected = {
        "words": {"total": 2, "unique": 2},
        "chars": {"total": 7, "unique": 7},
    }
    # execution
    output = word_count("abc def")
    # validation - word counts
    assert output["words"]["total"] == output["words"]["unique"]
    assert output["words"]["total"] == expected["words"]["total"]
    assert output["words"]["unique"] == expected["words"]["unique"]
    # validation - char counts
    assert output["chars"]["total"] == output["chars"]["unique"]
    assert output["chars"]["total"] == expected["chars"]["total"]
    assert output["chars"]["unique"] == expected["chars"]["unique"]


def test_total_counts_different_from_unique_counts():
    """Total and unique counts should be different when words are repeated"""
    # setup
    expected = {
        "words": {"total": 2, "unique": 1},
        "chars": {"total": 7, "unique": 4},
    }
    # execution
    output = word_count("abc abc")
    # validation - word counts
    assert output["words"]["total"] > output["words"]["unique"]
    assert output["words"]["total"] == expected["words"]["total"]
    assert output["words"]["unique"] == expected["words"]["unique"]
    # validation - char counts
