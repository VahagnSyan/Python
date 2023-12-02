"""
    Print characters from a string that are present at an even index number

"""

def print_even_index_value():
    text = input(f"Enter the string: ")

    for i in range(0, len(text), 2):
        print(text[i])

print_even_index_value()
