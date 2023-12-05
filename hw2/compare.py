def get_smaller_number(number1, number2):
    smaller_number = number1 if number1 - number2 == 0 else number2

    while (smaller_number - number1) * (smaller_number - number2) == 0:
        smaller_number -= 1

    return smaller_number

def compare_numbers(number1, number2):
    if number1 == number2:
        return 'E'
    diff = get_smaller_number(number1, number2) 
    for i in range(diff, number1):
        if i == number2:
            return number2
    return number1

num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))

result = compare_numbers(num1, num2)
if result == 'E':
    print("The numbers ae equal")
else:
    if num1 == result:
        print(f"{result} is lesser than {num2}")
    else:
        print(f"{result} is lesser than {num1}")
