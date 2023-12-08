''' 
    Guess the memorized number (1 - 100)
'''


from random import randint

def input_number():
    while True:
        num = input("Enter your number: ")
        if num.isdigit():
            return int(num)
        print("Invalid input! Please enter a number:")


def guess_number():
    print("Guess the number I memorized  between 1-100",)
    program_number = randint(1, 100)
    while True:
        user_number = input_number()
        if user_number == program_number:
            print("You win!")
            break
        elif user_number < program_number:
            print("Your number is less than my number!Try again.")
        else:
            print("Your number is greater than my number!Try again")


guess_number()    
