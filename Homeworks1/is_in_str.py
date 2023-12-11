"""
    Implement built-in function 
    is_in_str(str_obj, sub_string)
"""


def test_is_in_str():
    assert is_in_str("abcdef", "cd") == True

    assert is_in_str("abcdef", "gh") == False

    assert is_in_str("abcdef", "") == True

    assert is_in_str("abcdef", "abcdef") == True

    assert is_in_str("abcdef", "abcdefg") == False

    assert is_in_str("", "abc") == False

    assert is_in_str("", "") == True

    assert is_in_str("abcdef", "abc") == True

    assert is_in_str("abcdef", "def") == True

    assert is_in_str("ababab", "ab") == True

    print("All test cases passed successfully!")


def is_in_str(str_obj, sub_string):
    if not sub_string:
        return True

    first_match_index = str_obj.find(sub_string[0])

    if first_match_index == -1:
        return False

    if str_obj[first_match_index : first_match_index + len(sub_string)] == sub_string:
        return True
    else:
        return is_in_str(str_obj[first_match_index + 1 :], sub_string)


test_is_in_str()
