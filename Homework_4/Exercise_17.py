from random import randint

def get_valid_number():  # Check if the input number is valid
    while True:
        try:
            input_number = int(input("Enter the number: "))
            return input_number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def guess_number_game():  # A game about guessing a number between 0-100
    memorized_number = randint(0, 100)
    print("Welcome to guess number game!\n"
          "I memorized a number between 0 and 100.\n" 
          "You have to guess that number and I will help you.\n")
    
    while True:
        user_answer = get_valid_number()
        if user_answer == memorized_number:
            print("Congratulation!\tYOU WIN!!!")
            break
        elif user_answer > memorized_number:
            print(f"{user_answer} is bigger then memorized number! Try again.")
        else:
            print(f"{user_answer} is less then memorized number! Try again.")

if __name__ == '__main__':
    guess_number_game()