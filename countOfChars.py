'''

write a function that returns the number of non-overlapping occurrences of substring sub in string S
i.e. write a function that does the same as a builtin str.count() function does
function signature: count_sub_in_str(string_obj, substring)

'''

def count_sub_in_str(string, substring):
    count = 0
    len_substring = len(substring)
    for i in range(len(string) - len_substring + 1):
        if string[i:i + len_substring] == substring:
            count += 1
    return count

string_input = input("Input the string: ")
substring_input = input("Input the substring: ")
result = count_sub_in_str(string_input, substring_input)
print(f"Number of non-overlapping occurrences: {result}")

