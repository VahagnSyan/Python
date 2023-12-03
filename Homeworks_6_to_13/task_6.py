'''
    ex.6
    write a function that returns the number of non-overlapping occurrences
    of substring sub in string S i.e. write a function that does the same as 
    a builtin str.count() function does
    function signature: count_sub_in_str(string_obj, substring)
'''

def count_sub_in_str(str_obj, sub_str):
    count = 0
    str_len = len(str_obj)
    sub_len = len(sub_str)

    if sub_len <= str_len:
        i = 0
        while i <= str_len - sub_len:
            if str_obj[i:i + sub_len] == sub_str:
                count += 1
            i += 1

    return count

str_example = input('Enter the string: ')
sub_str_example = input('Enter the substring: ')

result = count_sub_in_str(str_example, sub_str_example)
print(f"The count of '{sub_str_example}' is: {result}")
