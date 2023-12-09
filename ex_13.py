'''
Գրեք ֆունկցիա, որը կստանա երկու ամբողջ թիվ ու կտպի թե այդ թվերից որն է մեծ, որը՝ փոքր, կամ՝ հավասար։
Ֆունցիան չպետք է օգտագործի համեմատության օպերատորներ։
'''


def mod(num_1 , num_2):
    dif = num_1 - num_2
    for i in range(num_1,num_2+1):
        if i == num_2 :
            return num_2
    return num_1    


number_1 = input("Enter number 1 :")

while not number_1.isdigit() :
     number_1 = input("Enter number 1 :")

number_2  = input("Enter number 2 :")

while not number_2.isdigit() :
    number_2 = input("Enter number 2 :")

number_1 = int(number_1)
number_2 = int(number_2) 

print(mod(number_1, number_2))

