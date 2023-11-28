""" ex6.py

write a function that returns the number of non-overlapping
occurrences of substring sub in string S
i.e. write a function that does the same as a builtin str.count() function does
function signature: count_sub_in_str(string_obj, substring)

"""

count = 0
def count_sub_in_str(string_obj, substring):
    global count
    if string_obj.find(substring) == -1: # if substring not in string_obj
        return count
    else: 
        count += 1
        return count_sub_in_str(string_obj[string_obj.find(substring) + len(substring):], substring)
        """
           call same function for string_obj and 
           starting search from after first funded substring.
        """

print("Count:", count_sub_in_str("abcbc", "bc"))
