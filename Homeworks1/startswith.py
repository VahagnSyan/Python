"""
    Implement built-in function 
    startswith(str_obj, sub_string)
"""


def test_startswith():
    assert startswith("hello", "he") == True, "Test Case 1 Failed"

    assert startswith("hello", "lo") == False, "Test Case 2 Failed"

    assert startswith("", "") == True, "Test Case 3 Failed"

    assert startswith("", "abc") == False, "Test Case 4 Failed"

    assert startswith("xyz", "") == True, "Test Case 5 Failed"

    assert startswith("abc", "abcdef") == False, "Test Case 6 Failed"

    assert startswith("python", "python") == True, "Test Case 7 Failed"

    print("All test cases passed!")


def startswith(str_obj, sub_string):
    # Checking if substring is the same as from 0 index to length of substring
    # And returning value
    return True if str_obj[0 : len(sub_string)] == sub_string else False


test_startswith()
