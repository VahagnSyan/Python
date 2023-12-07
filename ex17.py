import random

random_number = randint(1, 100);
input_number = input("Try guess the number(for end type 0): ")
while True:
    if input_number.isdigit():
        break
    else:
        input_number = input("Input number(for end type 0): ")
while input_number != 0:
    if input_number == random_number:
        print("Yes!!! You are guess the number")
        break
    elif input_number > random_number:
        # print("Your number is big than my")
        input_number = input("Your number is big than my enter anouter number(for end type 0): ")
        while True:
            if input_number.isdigit():
                break
            else:
                input_number = input("Input number(for end type 0): ")
    else:
        input_number = input("Your number is smol than my enter anouter number(for end type 0): ")
        while True:
            if input_number.isdigit():
                break
            else:
                input_number = input("Input number(for end type 0): ")