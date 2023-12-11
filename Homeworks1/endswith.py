"""
    Implement built-in function 
    endswith(str_obj, sub_string)
"""


def test_endswith():
    assert endswith("Hello, World!", "World!") == True

    assert endswith("Hello, World!", "Hello") == False

    assert endswith("", "") == True

    assert endswith("Hello, World!", "") == False

    assert endswith("Hello", "Hello, World!") == False

    assert endswith("Hello, World!", "world!") == False

    print("All test cases passed successfully!")


def endswith(str_obj, sub_string):
    # Checking if substring is the same startring from
    # substring length subtracted length of string
    # to end of string
    # and returning value
    return True if str_obj[-len(sub_string) :] == sub_string else False


test_endswith()
