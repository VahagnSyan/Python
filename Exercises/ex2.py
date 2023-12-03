'''
Remove first n characters from a string
Write a program to remove characters from a string starting from zero up to n and return a new string.
'''


input_string = input("Enter the string :")
number = input("Enter the number: ")

while not number.isdigit():
    number = input("Enter the number: ")

input_string = input_string[int(number):]
print(input_string)
