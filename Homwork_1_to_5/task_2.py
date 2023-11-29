'''
task 2
Remove first n characters from a string
Write a program to remove characters from a string starting from zero up to n and return a new string.
'''
# Define the string
string = 'Hello world!'
# Define the number of characters to remove
n = 5
''' Remove the first n characters from the string,
assign it to the variable 'string' '''
string = string[n:]
print(string)