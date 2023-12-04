'''
ex.2
Remove first n characters from a string
Write a program to remove characters from a string starting from zero up to n and return a new string.
'''

input_string = str(input("Input the string: "))
num_chars_to_remove = int(input("Input the number of characters you want to remove: "))

print(input_string)
modified_string = input_string[num_chars_to_remove:]
print(modified_string)

