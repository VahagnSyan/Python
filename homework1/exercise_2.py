"""
    Remove first n characters from a string
    Write a program to remove characters from a string starting from zero up to n and return a new string.

"""

def remove_chars(string, n):
    new_string = string[n:]
    return new_string


def get_valid_number():  # Check if the input number is valid
    while True:
        try:
            input_number = int(input("Enter the number: "))
            return input_number
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    text = input("Enther text: ")
    boarder = get_valid_number()
    result = remove_chars(text, int(boarder))
    print(result) 

main()