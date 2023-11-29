'''
The program takes number and print all prime numbers that are less than him
'''
       
def is_prime(num):
    if num == 1 or num == 2:
        return False
    elif num > 2:
        for i in range(3, num):
            if num % i == 0:
                return False
        return True

def print_prime(number):
    if number <= 2:
        print("There are no prime numbers less than or equal to 2")
    else:
        print("Prime numbers less than or equal to", number, "are: ")
        for i in range(3, number + 1):
            if is_prime(i):
                print(i, end=" ")
        print()

while True:  # infinite loop untill user input is valid
    try:     # trying to catch exceptions
        user_input = int(input("Enter a number: "))
        break            # if user input valid number -> break
    except ValueError:   # this line is responsible for catching exceptions
        print("Invalid input. Please enter a valid integer.")   # if exception was caught write
                                                                # helping msg to user
print_prime(user_input)
