''' ex1.py

	Display numbers divisible by 5 from a list

	Given list is  [10, 20, 33, 46, 55]
	Divisible by 5
	10
	20
	55
'''


input_list = [10, 20, 33, 46, 55]
div = input("Enter Divisible number: ")
while True:
	if div.isdigit(): # checking input divisible number is integer or not
		break
	else:
		div = input("Enter Divisible number: ")

for i in input_list:
    if i % int(div) == 0:
        print(i)

