# Check Palindrome Number


def is_palindrome_number(number):
    try:
        number = int(number)
    except ValueError:
        return print("Error: Please enter a valid integer .")

    return str(number) == str(number)[::-1]


n = input("Enter the number: ")

print(f"The number {n} is palindrome: {is_palindrome_number(n)}.")
