# Remove first n characters from a string
# Write a program to remove characters from a string
# starting from zero up to n and return a new string.


def remove_first_n_characters(input_string, n):
    try:
        n = int(n)
    except ValueError:
        return "Error: Please enter a valid integer ."

    if n >= len(input_string):
        return "Error: n is greater than or equal to the string length."

    new_string = input_string[n:]

    return new_string


original_string = input("Enter a string: ")

n = input("Enter the number of characters to remove: ")

result = remove_first_n_characters(original_string, n)


print(f"After removing {n} characters: {result}")
