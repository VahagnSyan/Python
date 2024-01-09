def mmap(func, *iterable):
    for items in zip(*iterable):
        yield func(*items)

def add(*nums):
    return sum(nums)

def mul(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

l1 = [1, 2, 3, 4, 5]
l2 = [1, 3, 5]
l3 = [2, 3, 4]
l4 = [5, 6, 7, 9]

result_iterator = mmap(add, l1, l2, l3)
print(f"Result of sum:")
for result in result_iterator:
    print(result)

result_iterator = mmap(mul, l1, l2, l3, l4)
print(f"Result of multipl...:")
for result in result_iterator:
    print(result)
