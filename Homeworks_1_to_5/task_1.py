'''
    task 1
    Given list is  [10, 20, 33, 46, 55]
    Divisible by 5
    10
    20
    55
'''


def get_number_list_input():
    while True:
        user_input = input("Enter a list of numbers separated by spaces: ")
        if all(char.isdigit() or char.isspace() for char in user_input):
            return [int(num) for num in user_input.split()]

        print("Invalid input. Please enter numbers separated by spaces.")


input_list = get_number_list_input()

print("Divisible by 5:")
for i in input_list:
    if i % 5 == 0:
        print(i)
