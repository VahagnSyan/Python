""" ex13.py
    Գրեք ֆունկցիա, որը կստանա երկու ամբողջ թիվ ու կտպի թե այդ թվերից որն է մեծ,
    որը՝ փոքր, կամ՝ հավասար։
    Ֆունցիան չպետք է օգտագործի համեմատության օպերատորներ։
"""

def comparison(num1, num2):
    dif = num1 - num2
    _abs_ = abs(num1 - num2)
    if not dif: # num1 - num2 = 0 => False. if not False => ("Equal")
        print("Equal")
    elif not id(dif) - id(_abs_):
        # if addres (__dif__) == addres (_abs_)
        # f.e. addres (7 - 5) - addres |7 - 5| = 0
        print(f"{num1} > {num2}")
    else:
        print(f"{num1} < {num2}")

def input_number(symbol):
    while True:
        try:
            num = int(input(f"Input {symbol}: "))
            return num
        except:
            print(f"Invalid input. Please enter a valid number for {symbol}.")

comparison(input_number("first number"), input_number("second number"))

