from random import randint

def is_input(inp):
    if inp.isdigit() and int(inp) > 0:
        inp = int(inp)
        return inp
    else:
        return is_input(input("Input a valid number 1, 100 (for end, type 0): "))

random_number = randint(1, 100)
input_number = is_input(input("Input a number 1, 100 (for end, type 0): "))

while input_number != 0:
    if input_number == random_number:
        print("Yes!!! You guessed the number")
        break
    elif input_number > random_number:
        input_number = is_input(input("Your number is greater than my secret number. Enter another number (for end, type 0): "))
    else:
        input_number = is_input(input("Your number is smaller than my secret number. Enter another number (for end, type 0): "))
