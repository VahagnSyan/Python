def my_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i
    
filtered_nums = my_filter(lambda x: x % 2 == 0, range(0, 30))

for i in filtered_nums:
    print(i)

