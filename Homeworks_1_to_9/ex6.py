""" ex6.py

	write a function that returns the number of non-overlapping
	occurrences of substring sub in string S
	i.e. write a function that does the same as a builtin str.count() function does
	function signature: count_sub_in_str(string_obj, substring)
"""

def count_sub_in_str(string_obj, substring):
	count = 0
	if substring in string_obj:
		for i in range(0, len(string_obj) - len(substring) + 1):
			if string_obj[i:i + len(substring)] == substring:
				count += 1
	return count
	
print("Count:", count_sub_in_str("abcbcgdfgdbc", "bc"))

