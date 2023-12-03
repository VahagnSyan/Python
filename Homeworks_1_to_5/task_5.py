'''
    Check Palindrome Number
    Write a program to check if the given number is a palindrome number.
    A palindrome number is a number that is the same after reverse.
    For example, 545, is the palindrome numbers
    DO NOT use reverse builtin function.
'''
num = input('Enter the number: ')
while True:
    if num.isdigit():
        break
    else:
        num = input('The number must be an integer: ')

if num == num[::-1]:
    print("The number is a palindrome!")
else:
    print("The number is not a palindrome!")
