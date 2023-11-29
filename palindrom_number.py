"""
ex.5
Check Palindrome Number
Write a program to check if the given number is a palindrome number.
A palindrome number is a number that is the same after reverse.
For example, 545, is the palindrome numbers
"""
number = int(input("number = "))

num_str = str(number)

if num_str == num_str[::-1]:
    print("the number is palondrom")
else:
    print("the number is not palindrom")

