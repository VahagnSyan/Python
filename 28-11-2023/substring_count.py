'''
The program calculate the count of substr in str
'''


str = input("Enter the str: ") 
substr = 'l'
count = 0
for i in str:
    if i == substr:
        count += 1

print(f"Count of {substr} substr -", count)
