"""
Check Palindrome Number
Write a program to check if the given number is a palindrome number.
A palindrome number is a number that is the same after reverse.
For example, 545, is the palindrome numbers
DO NOT use reverse builtin function.
"""

input_number = 545 # Magic value

# Convert number to string to iterate over elements
string_number = str(input_number)

is_palindrome = True;

for i in range(0, len(string_number)):
    if(string_number[i] != string_number[len(string_number) - 1 - i]):
        # Comparing ith element to corresponding
        # ith element from the end of string
        # If they are not the same then the number is not palindrome.

        is_palindrome = False;
        break


# Using ternary operator to print result text based on is_palindrome value
print("Number is palindrome" if is_palindrome else "Number is not palindrome")