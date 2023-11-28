numbers = []

print("Enter quantity of elements: ")
quantity = int(input())

for num in range(quantity):
    print(f"Enter value for array[{num}]: ", end=" ")
    numbers.append(int(input()))

print("Enter divisor: ")
divisor = int(input())

print(f"Numbers divisible by {divisor}:")

for num in numbers:
    if num % divisor == 0:
        print(num)
