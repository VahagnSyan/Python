'''
Check Palindrome Number
Write a program to check if the given number is a palindrome number.
A palindrome number is a number that is the same after reverse.
For example, 545, is the palindrome numbers
DO NOT use reverse builtin function.
'''


def is_palindrome_number(number):

    return number== number[::-1]


num = input("Enter  number : ")
while not num.isdigit():
    num = input("Enter  number : ")

print(f"The number {num} is palindrome: {is_palindrome_number(num)}.")
