'''
Remove first n characters from a string
Write a program to remove characters from a string
starting from zero up to n and return a new string.
'''


def remove_first_n_characters(input_string, num):
    num = int(num)
    if num >= len(input_string):
        print("\nn is greater than or equal to the string length.")
    new_string = input_string[num:]
    return new_string

original_string = input("Enter a string: ")
num = input("Enter the number of characters to remove: ")

while not num.isdigit():
    num = input("Enter the number of characters to remove: ")

while int(num) >= len(original_string):
    print("\nn is greater than or equal to the string length.Try again")
    num = input("Enter the number of characters to remove: ")
    while not num.isdigit():
        num = input("Enter the number of characters to remove: ")

result = remove_first_n_characters(original_string, num)
print(f"After removing {num} characters: {result}")
