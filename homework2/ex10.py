"""
    Գրեք այնպիսի ֆունկցիա, որը ստանում է  ամբողջ թիվ և տպում այդ թվից փոքր կամ հավասար բոլոր պարզ թվերը:
    Պարզ թիվը 1-ից մեծ դրական ամբողջ թիվ է, որը բաժանվում է միայն իր և 1-ի վրա:

"""

def prime_numbers(number):
    for num in range(2, number+1):
        flag_prime = True

        for i in range(2, int(num/2) + 1):
            if num % i == 0:
                flag_prime = False
                break

        if flag_prime:
            print(num)


def get_valid_number():  # Check if the input number is valid
    while True:
        try:
            input_number = int(input("Enter the number: "))
            return input_number
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    number = get_valid_number()
    prime_numbers(int(number))

main()