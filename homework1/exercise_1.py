"""
Display numbers divisible by 5 from a list

"""

def input_array():
    array = []
    print("Enter numbers (type 'done' to finish):")

    while True:
        user_input = input("Enter a number: ")

        if user_input.lower() == 'done':
            break
        
        array.append(int(user_input))

    print("The numbers entered are:", array)
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
