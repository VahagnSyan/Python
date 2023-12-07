from random import randint

def guess_number():
    target = randint(1, 100)
    print("Welcome to the Number Guessing Game!")

    attempt = 0

    while True:
        try:
            user_input = int(input("Enter your guess: "))
            attempt += 1

            if user_input == target:
                print(f"Congrats! You guessed the number in {attempt} attempts ")
                break
            elif user_input < target:
                print("Ahh nearly. try greater number")
            else:
                print("Ahh nearly. Try lower number")

        except ValueError:
            print("Invalid Input. Please enter valid number ")

guess_number()
