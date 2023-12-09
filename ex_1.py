'''
Display numbers divisible by 5 from a list
'''


user_input = input("Enter a list of numbers separated by space: ")
input_list = user_input.split()
num_list = []

for item in input_list:
    try:
        num_list.append(int(item))
    except ValueError:
        print(f"Skipping '{item}' as it is not a valid integer.")
for i in num_list:
    if i % 5 == 0:
        print(i)
