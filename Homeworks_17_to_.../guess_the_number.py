""" 
    Guess the number from (1 to 100)
"""


import random


def guess_the_number():
    print("------- Guess The Number ------",)
    print("        From (1 to 100)       \n")
    program_number = random.choice(range(1, 101))
    while True:
        user_number = input_number()
        if user_number == program_number:
            print(f"----- You have won: Number is {program_number} -----")
            break
        elif user_number < program_number:
            print("Your number is less than the program number.")
        else:
            print("Your number is greater than the program number.")

def input_number():
    num = input("Enter the number: ")
    while True:
        if num.isdigit():
            return int(num)
        else:
            num = input("Enter the number: ")


guess_the_number()    

