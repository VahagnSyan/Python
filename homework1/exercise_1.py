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
    array = []
    quantity = get_valid_number()

    for i in range(0, quantity):
        input_number = input("Enter the number: ")
        while not input_number.isdigit():
            input_number = input("Enter the number: ")

        
        array.append(int(input_number))

    print("The entered numbers are:", array)
    return array

def check_divisibility(numbers):
    divisible = get_valid_number()

    for i in range(0, len(numbers)):
        if numbers[i] % divisible == 0:
            print(f"Numbers divisible by {divisible}:")
            print(numbers[i])

def main():
    numbers = input_array()
    check_divisibility(numbers)

main()
