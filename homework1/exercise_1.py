"""
    Display numbers divisible by 5 from a list

"""
def get_valid_number():  # Check if the input number is valid
    while True:
        try:
            input_number = int(input("Enter the number: "))
            return input_number
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def input_array():
    quantity = get_valid_number()
    array = [get_valid_number() for _ in range(quantity)]
    print("The entered numbers are:", array)

    return array


def check_divisibility(numbers):
    divisible = get_valid_number()
    print(f"Numbers divisible by {divisible}:")

    for i in range(0, len(numbers)):
        if numbers[i] % divisible == 0:  
            print(numbers[i], end = ' ')
    else:
        print('None')


def main():
    numbers = input_array()
    check_divisibility(numbers)

main()
