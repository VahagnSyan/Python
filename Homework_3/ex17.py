import random

def guess_number():
    stored_number = random.randint(0, 100)
    while True:
        input_number = int(input("Enter the number :"))
        if input_number == stored_number:
            print("Congratulation you guess the number!!!")   
            break      
        elif input_number > stored_number:
            print("It's big")
        elif input_number < stored_number:
            print("It's small")

print("Guess the memorized number between 0 to 100")
guess_number()
    