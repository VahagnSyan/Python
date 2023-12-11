"""
    Count letters in string and add them to dictionary
"""


def test_count_letters():
    input_str = "hello"
    expected_output = {"h": 1, "e": 1, "l": 2, "o": 1}
    assert count_letters(input_str) == expected_output

    input_str = ""
    expected_output = {}
    assert count_letters(input_str) == expected_output

    input_str = "programming"
    expected_output = {"p": 1, "r": 2, "o": 1, "g": 2, "a": 1, "m": 2, "i": 1, "n": 1}
    assert count_letters(input_str) == expected_output

    input_str = "hello world!"
    expected_output = {
        "h": 1,
        "e": 1,
        "l": 3,
        "o": 2,
        " ": 1,
        "w": 1,
        "r": 1,
        "d": 1,
        "!": 1,
    }
    assert count_letters(input_str) == expected_output

    print("All test cases passed!")


def count_letters(string):
    letters_count = {}

    for char in string:
        letters_count[char] = string.count(char)

    return letters_count


test_count_letters()
