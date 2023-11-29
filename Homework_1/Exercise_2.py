"""Write a program 
to remove characters from a string 
starting from zero up to n and return a new string.
"""


input_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
remove_number = input("Enter the number: ")
while not remove_number.isdigit():
    remove_number = input("Enter the number: ")

input_string = input_string[int(remove_number):]
print("New string: \n" + input_string)