'''
    ex. 17
    Guess the memorized number
'''

from random import randint

def guess_the_number(entered_num, stored_num):
    if entered_num == stored_num:
        print("Congratulations! You guessed the correct number.")
        return True
    elif stored_num > entered_num:
        print('Your guess is too low. Try a higher number.')
    else:
        print('Your guess is too high. Try a lower number.')
    return False

stored_num = randint(1, 100)
print("I have selected a number between 1 and 100. Can you guess it?")

while True:
    input_num = input("Enter your guess: ")
    if input_num.isdigit():
        entered_num = int(input_num)

        if 1 <= entered_num <= 100:
            result = guess_the_number(entered_num, stored_num)

            if result:
                break
        else:
            input_num_str = input("Invalid input! Please enter a number in the range [1, 100]. ")
    else:
        input_num_str = input("Invalid input! Please enter an integer. ")


    