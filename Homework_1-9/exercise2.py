'''
    Remove first n characters from a string
    Write a program to remove characters from 
    a string starting from zero up to n and return a new string.
'''

string = input("Enter a string: ")
n = int(input("Enter the index: "))  
substring = string[n:]  
print(substring)
