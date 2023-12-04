'''
ex.5
Check Palindrome Number
Write a program to check if the given number is a palindrome number.
A palindrome number is a number that is the same after reverse.
For example, 545, is the palindrome numbers
DO NOT use reverse builtin function.
'''

def is_palindrome(number):
    i = 0
    while i <= len(number) // 2:
        if number[i] == number[len(number) - i - 1]:
            i += 1
        else:
            return False
    return True

valid_input = False
while not valid_input:
    number = input("Input the number: ")
    if number.isdigit():
        valid_input = True
    else:
        print("Invalid input. Please enter a valid integer.")

if is_palindrome(number):
    print(f"The {number} is a palindrome")
else:
    print(f"The {number} is not a palindrome")

