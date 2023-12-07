'''
ex.4
Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5

'''

while True:
    number = input("Enter a number: ")
    if number.isdigit():
        number = int(number)
        if number > 0:
            for i in range(1, number+1):
                for j in range(i):
                    print(i, end = " ")
                print()
            break
        else:
            print("Please enter a non-negative integer.")
    else:
        print("Invalid input. Please enter a valid number.")
