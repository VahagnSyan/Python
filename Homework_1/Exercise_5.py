"""Check Palindrome Number
Write a program to check if the given number is a palindrome number.
A palindrome number is a number that is the same after reverse.
For example, 545, is the palindrome numbers
DO NOT use reverse builtin function.
"""


input_number = input("Enter the number: ")
while not input_number.isdigit():
    input_number = input("Enter the number: ")

if input_number == input_number[::-1]:
    print("The given number is polindrome:")
else:
    print("The given number is not polindrome:")

input_number = int(input_number)