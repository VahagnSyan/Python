"""
    Check Palindrome Number
    Write a program to check if the given number is a palindrome number.
    A palindrome number is a number that is the same after reverse.
    For example, 545, is the palindrome numbers
    DO NOT use reverse builtin function.
"""


def test_is_palindrome():
    assert is_palindrome(121) == True

    assert is_palindrome(123) == False

    assert is_palindrome(7) == True

    assert is_palindrome(123321) == True

    assert is_palindrome(-121) == False

    assert is_palindrome(0) == True

    print("All test cases passed.")


def is_palindrome(number):
    # Convert number to string to iterate over elements
    string_number = str(number)

    is_palindrome = True

    for i in range(0, len(string_number)):
        if string_number[i] != string_number[len(string_number) - 1 - i]:
            # Comparing ith element to corresponding
            # ith element from the end of string
            # If they are not the same then the number is not palindrome.

            is_palindrome = False
        break
    return is_palindrome


test_is_palindrome()
