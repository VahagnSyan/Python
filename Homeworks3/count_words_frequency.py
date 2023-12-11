"""
    Count words in string and add them to dictionary
"""


def test_count_words():
    assert count_words("") == {}

    assert count_words("hello") == {"hello": 1}

    assert count_words("The quick brown fox jumps over the lazy dog") == {
        "The": 1,
        "quick": 1,
        "brown": 1,
        "fox": 1,
        "jumps": 1,
        "over": 1,
        "the": 1,
        "lazy": 1,
        "dog": 1,
    }

    assert count_words("Apple apple aPpLe") == {"Apple": 1, "apple": 1, "aPpLe": 1}

    print("All test cases passed!")


def count_words(string):
    words_count = {}
    splitted_string = string.split()

    for word in splitted_string:
        words_count[word] = string.count(word)

    return words_count


test_count_words()
