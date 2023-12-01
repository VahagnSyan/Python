"""
    Display numbers divisible by 5 from a list
"""


def input_list():
    while True:
        try:
            input_string = input("Enter elements of the list separated by spaces: ")

            elements = input_string.split()

            # Converts every element to int
            elements = [int(element) for element in elements]

            break
        except ValueError:
            # If ValueError happens program asks for new input
            print("Error: Please enter numbers.")

    return elements


nums = input_list()

for num in nums:
    # Iterating over numbers and checking if they are divisible by 5
    if num % 5 == 0:
        print(num)
