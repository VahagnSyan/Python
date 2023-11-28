''' ex1.py

Display numbers divisible by 5 from a list

Given list is  [10, 20, 33, 46, 55]
Divisible by 5
10
20
55
'''


input_list = [10, 20, 33, 46, 55]
div = int(input("Enter Divisible number: "))
for i in input_list:
    if i % div == 0:
        print(i)

