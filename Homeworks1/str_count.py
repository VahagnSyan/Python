"""
    Write a function that returns the number of non-overlapping
    occurrences of substring sub in string i.e. write a function
    that does the same as a builtin str.count() function does
    function signature: count_sub_in_str(string_obj, substring)
"""


def test_count_sub_in_str():
    assert count_sub_in_str("hello world", "world") == 1

    assert count_sub_in_str("hello world, world!", "world") == 2

    assert count_sub_in_str("abcdefg", "xyz") == 0

    assert count_sub_in_str("abcabcabc", "abc") == 3

    assert count_sub_in_str("xyzxyzxyz", "xyz") == 3

    print("All test cases passed!")


def count_sub_in_str(string_obj, substring):
    if not substring:
        return len(string_obj)

    count = 0
    i = 0

    while i < len(string_obj):
        index = string_obj.find(substring, i)
        if index != -1:
            # If substring is present, add 1 to count
            # and start the next iteration after substring index
            count += 1
            i = index + len(substring)
        else:
            i += 1
    return count


test_count_sub_in_str()
