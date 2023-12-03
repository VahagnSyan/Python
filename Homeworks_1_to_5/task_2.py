'''
    task 2
    Remove first n characters from a string
    Write a program to remove characters from a string starting from zero up to n and return a new string.
'''
str_obj = input('Enter the string: ')
rm_count = input('Enter the count of remove elements: ')

while True:
    if rm_count.isdigit():
        rm_count = int(rm_count)
        break
    rm_count = input('The count of remove elements must be an integer: ')

str_obj = str_obj[rm_count:]

print(str_obj)
