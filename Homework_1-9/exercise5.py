'''
    Check Palindrome Number
    Write a program to check if the given number is a palindrome number.
    A palindrome number is a number that is the same after reverse.
    For example, 545, is the palindrome numbers
    DO NOT use reverse builtin function.
'''

def input_num():
    while True:
        num = input("Enter a number: ")
        if num.isdigit() and int(num) > 1:
            return int(num)
        print("Invalid input! Please enter a number greater than 1:")

def check_palindrome(num):
    num_str = str(num)  # Convert the number to a string

    if num_str == num_str[::-1]:  # Check if the string is equal to its reverse
        print("The number is a palindrome")
    else:
        print("The number is not a palindrome")


number = input_num()
check_palindrome(number)


