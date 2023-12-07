""" 
    Guess number game.
"""

from random import randint


def input_number():
    number = input("Guess the number: ")

    while number.isdigit() == False:
        number = input("Guess the number: ")

    return int(number)


def guess_number():
    generated_number = randint(1, 101)

    while True:
        number = input_number()
        if number == generated_number:
            print(f"You are correct! Generated number is - {generated_number}")
            break
        elif number > generated_number:
            print("Generated number is less than your guess")
        else:
            print("Generated number is greater than your guess")


guess_number()
