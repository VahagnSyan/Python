import random

def input_int(prompt="Input the number: "):
    while True:
        number_str = input(prompt)
        if number_str.isdigit():
            return int(number_str)
        else:
            print("Please enter a valid integer.")

def guess_the_number():
    print("I have chosen a random number"
        "between 1 and 10. Guess it.")

    secret_number = random.randint(1, 10)

    attempts = 0

    while True:
        guess = input_int("Enter your guess: ")
        attempts += 1

        if guess == secret_number:
            print("Wow!!! You guessed the number"
                    f" in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

guess_the_number()

