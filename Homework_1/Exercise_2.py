"""Write a program 
to remove characters from a string 
starting from zero up to n and return a new string.
"""

input_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
n = int(input("Enter the number: "))
input_string = input_string[n:]
print("New string: \n" + input_string)