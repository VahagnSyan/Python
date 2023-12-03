"""
    Check Palindrome Number

"""

def is_palindrome(num):
    num_str = str(num)
    length = len(num_str)

    for i in range(length // 2):
        if num_str[i] != num_str[-1-i]:
            return False

    return True


def get_valid_number():  # Check if the input number is valid
    while True:
        try:
            input_number = int(input("Enter the number: "))
            return input_number
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    number = get_valid_number()

    if is_palindrome(int(number)):
        print(f"{number} is a palindrome number")
    else:
        print(f"{number} is not a palindrome number")


main()
