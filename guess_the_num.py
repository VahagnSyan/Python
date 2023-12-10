"""
Ex.
Guess the random number
"""


from random import randint

target = randint(1, 100)
print("guess the number from 1 to 100")

while True:
    input_number = input("Enter the number: ")
    if input_number.isdigit():
        input_num = int(input_number)
        if input_num == target:
            print("Congratulations! You guessed the number correctly!")
            break
        elif input_num > target:
            print("Try a smaller number.")
        else:
            print("Try a larger number.")
    else:
        print("Invalid input. Please enter a valid number.")

