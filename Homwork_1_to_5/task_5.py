'''
Check Palindrome Number
Write a program to check if the given number is a palindrome number.
A palindrome number is a number that is the same after reverse.
For example, 545, is the palindrome numbers
DO NOT use reverse builtin function.
'''
# Define the numper
num = 545
# Store the original number for comparison
original_number = num
# Define  a variable to store the reversed number
reversed_number = 0

# Loop to reverse the digits of the number
while num > 0:
    # Extract the last digit of the number
    digit = num % 10
    # Add the digit to the reversed number in the reverse order
    reversed_number = reversed_number * 10 + digit
    # Remove the last digit from the original number
    num //= 10

# Check if the numbers are equal
if original_number == reversed_number:
    print("The number is a palindrome!")
else:
    print("The number is not a palindrome!")