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


def main():
    number = input("Enter a number: ")

    while not number.isdigit():
        number = input("Enter a number: ")


    if is_palindrome(int(number)):
        print(f"{number} is a palindrome number")
    else:
        print(f"{number} is not a palindrome number")

main()
