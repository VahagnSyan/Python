"""
    Print characters from a string that are
    present at an even index number
    Orginal String is  test_text
    Printing only even index chars
"""


def test_print_even_index_chars():
    assert print_even_index_chars("test_text") == "ts_et"

    assert print_even_index_chars("") == ""

    assert print_even_index_chars("a") == "a"

    assert print_even_index_chars("!@#$%^&*()") == "!#%&("

    print("All test cases passed successfully!")


def print_even_index_chars(string):
    result_string = ""

    for i in range(0, len(string)):
        # Iterating over string and checking if they are even
        if i % 2 == 0:
            result_string += string[i]

    return result_string


# print(print_even_index_chars("test_text"))
test_print_even_index_chars()
