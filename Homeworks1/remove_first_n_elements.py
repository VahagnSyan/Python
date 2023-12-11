"""
    Remove first n characters from a string
    Write a program to remove characters from
    a string starting from zero up to n and return a new string.
"""


def test_remove_characters():
    assert remove_first_n_characters("Hello World", 3) == "lo World"

    assert remove_first_n_characters("Python", 5) == "n"

    assert remove_first_n_characters("abcdef", 0) == "abcdef"

    assert remove_first_n_characters("", 10) == ""

    print("All test cases pass!")


def remove_first_n_characters(input_string, characters_count):
    return input_string[characters_count:]


test_remove_characters()
