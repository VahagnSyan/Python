def mmap(func, iterable1, iterable2):
    for item1, item2 in zip(iterable1, iterable2):
        yield func(item1, item2)

def add(num1, num2):
    return num1 + num2

def mul(num1, num2):
    return num1 * num2

l1 = [1, 2, 3, 4, 5]
l2 = [1, 3, 5]

result_iterator = mmap(add, l1, l2)

for result in result_iterator:
    print(result)
