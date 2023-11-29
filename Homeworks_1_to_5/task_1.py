'''
task 1
Given list is  [10, 20, 33, 46, 55]
Divisible by 5
10
20
55
'''
# Define a list of numbers
input_list = [10, 20, 33, 46, 55]
#Loop through the elements
for i in input_list:
    # Check if the number is divisible by 5 without a remainder
    if i%5 == 0:
        print(i)