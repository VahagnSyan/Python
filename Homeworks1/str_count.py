"""
    Write a function that returns the number of non-overlapping
    occurrences of substring sub in string i.e. write a function
    that does the same as a builtin str.count() function does
    function signature: count_sub_in_str(string_obj, substring)
"""

input_string = "Hello World!" # Magic Value
input_substring = "ll" # Magic Value

def count_sub_in_str(string_obj, substring):
    count = 0
    i = 0

    while i < len(string_obj):
        index = string_obj.find(substring, i)
        if index != -1:
            # If substring is present add 1 to count
            # and start next iteratrion after substring index
            count += 1
            i = index + len(substring)
        else:
            return count
    return count



print(count_sub_in_str(input_string, input_substring))