'''
Check Palindrome Number
'''

number = input("Enter the number :")
is_polindrome = False

for i in range(len(number) // 2):
    if number[i] == number[len(number) - i - 1]:
        is_polindrome = True
        break

if is_polindrome:
    print("The given number is polindrome")
else:
    print("The given number is't polindrome")
    