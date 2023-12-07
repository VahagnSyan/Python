'''
ex.6
write a function that returns the number of non-overlapping occurrences of substring sub in string S
i.e. write a function that does the same as a builtin str.count() function does
function signature: count_sub_in_str(string_obj, substring)
'''


def count_sub_in_str(string_obj, substring):
    count = 0
    len_substring = len(substring)
    i = 0
    while i <= len(string_obj) - len_substring:
        if string_obj[i:i + len_substring] == substring:
            count += 1
            i += len_substring
        else:
            i += 1
    return count
string_obj = str(input("Enter a word: "))
substring = str(input("Enter searching combination: "))
result = count_sub_in_str(string_obj, substring)
print(f"The number of non-overlapping occurrences of '{substring}' in '{string_obj}' is: {result}")
