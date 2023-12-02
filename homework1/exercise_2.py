"""
    Remove first n characters from a string
    Write a program to remove characters from a string starting from zero up to n and return a new string.

"""

def remove_chars(string, n):
    new_string = string[n:]
    return new_string

def main():
    text = input("Enther text: ")
    boarder = input("Enter boarder: ")

    while not boarder.isdigit():
        boarder = input("Enter the number: ")

    result = remove_chars(text, int(boarder))
    print(result) 

main()