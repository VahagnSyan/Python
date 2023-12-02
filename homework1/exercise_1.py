"""
    Display numbers divisible by 5 from a list

"""

def input_array():
    array = []
    quantity = int(input("Enter quantity of array elements: "))

    for i in range(0, quantity):
        input_number = input("Enter the number: ")
        while not input_number.isdigit():
            input_number = input("Enter the number: ")

        
        array.append(int(input_number))

    print("The entered numbers are:", array)
    return array

def check_divisibility(numbers):
    divisible = int(input("Enter the divisible : "))

    for i in range(0, len(numbers)):
        if numbers[i] % divisible == 0:
            print(f"Numbers divisible by {divisible}:")
            print(numbers[i])

def main():
    numbers = input_array()
    check_divisibility(numbers)

main()
