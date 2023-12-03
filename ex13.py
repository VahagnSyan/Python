'''
This function compares two  given numbers
'''

Num1=int(input("Enter the first number:\n"))
Num2=int(input("Enter the second number: \n"))

Num3=Num1-Num2
if Num3==0:
    print("the numbers are EQUAL!")
else:
    num_bit=(Num3>>31)&1 
    if num_bit:
        print("the bigger is:\n")
        print(eval('Num2'))
    else:
        print("the bigger is:\n")
        print(eval('Num1'))

