"""
    Գրեք ֆունկցիա, որը կստանա երկու ամբողջ թիվ ու կտպի թե այդ թվերից որն է մեծ, որը՝ փոքր, կամ՝ հավասար։
    Ֆունցիան չպետք է օգտագործի համեմատության օպերատորներ։

"""

    
def find_max(num1, num2):

    if (not(num1 - num2)):     # if num1 = num2
        print(f"{num1} = {num2}")
    
    elif (not(num2)):   # if num2 == 0
        if (not(num1 + abs(num1))):
            print(f"{num2} > {num1}")
        else:
            print(f"{num1} > {num2}")
    
    elif (not(num1 + abs(num1)) and not(num2 + abs(num2))):   # if num1 and num2 < 0
        if(num1 // num2):
            print(f"{num2} > {num1}")
        else:
            print(f"{num1} > {num2}")
    
    elif(num1+abs(num1) and num2+abs(num2)):    # id num1 and num2 > 0 
        if(num1 // num2):
            print(f"{num1} > {num2}")
        else:
            print(f"{num2} > {num1}")
    
    elif(not(num1 + abs(num1))):    # if num1 < 0, num2 > 0   
        print(f"{num2} > {num1}")

    else:   # if num1 < 0, num2 >0
        print(f"{num1} > {num2}")


def get_valid_number():  # Check if the input number is valid
    while True:
        try:
            input_number = int(input("Enter the number: "))
            return input_number
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    input_number1 = get_valid_number()
    input_number2 = get_valid_number()
    
    find_max(int(input_number1), int(input_number2))

main()

