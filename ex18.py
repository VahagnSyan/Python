'''
function to find a random number!
'''

import random
number=random.randrange(0, 100)
#print(number)
find_number = int(input("enter the number to find a random between 0 - 100:\n"))
while find_number != number:
    if find_number < number:
        print("random is bigger then you number.")
        find_number =  int(input("Enter again!\n"))
    if find_number > number:
        print("random is smaller then you number.")
        find_number =  int(input("Enter again!\n"))
print("You find it! ", "RANDOM=", number)