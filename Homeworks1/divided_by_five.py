"""Display numbers divisible by 5 from a list"""

nums = [10, 20, 33, 46, 55] # Magic value

for num in nums:
    # Iterating over numbers and checking if they are divisible by 5
    if(num % 5 == 0):
        print(num)