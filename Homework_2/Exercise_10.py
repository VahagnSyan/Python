"""
Գրեք այնպիսի ֆունկցիա, որը ստանում է  ամբողջ թիվ 
և տպում այդ թվից փոքր կամ հավասար բոլոր պարզ թվերը:
Պարզ թիվը 1-ից մեծ դրական ամբողջ թիվ է, 
որը բաժանվում է միայն իր և 1-ի վրա:
"""


def get_valid_number():  # Check if the input number is valid
    while True:
        try:
            input_number = int(input("Enter the number: "))
            return input_number
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
def print_prime_numbers(number):
    if number < 2:
        print("No prime numbers")
    else:
        print("Prime numbers up to", str(number) + ":")
        for i in range(2, number + 1):
            dividers_count = True
            for j in range(2, int(i**0.5) + 1):  # Checks if the number has another divisor
                if i % j == 0:
                    dividers_count = False
                    break
            
            if dividers_count:
                print(i, end=" ")

input_number = get_valid_number()

print_prime_numbers(int(input_number))