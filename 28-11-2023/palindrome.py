'''
The program checks if the inputed value is palindrome or not
'''


number = input("Enter the number: ") 
print("Your number -", number) 
if number == number[::-1]:  # checks with the reversed version
    print("Your number is palindrome ")
else:
    print("Your number isn`t palindrome ")
    
