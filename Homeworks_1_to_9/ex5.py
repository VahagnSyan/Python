""" ex5.py

	Check Palindrome Number
	Write a program to check if the given number is a palindrome number.
	A palindrome number is a number that is the same after reverse.
	For example, 545, is the palindrome numbers
	DO NOT use reverse builtin function.

"""

number = input("Enter the number: ")

while True: # checking number is integer or not
	if number.isdigit():
		break
	else:
		number = input("Enter the number: ")

number = int(number)
if str(number)[:] == str(number)[::-1]:
    print(f"{number} is a polindrom")
else:
    print(f"{number} isn\'t polindrom")

