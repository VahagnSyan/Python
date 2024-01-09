def lists_sum(*iterable):
    for i in zip(*iterable):
        yield sum(i)

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4, 5]
list3 = [1, 2]

result_iterator = lists_sum(list1, list2, list3)

for i in result_iterator:
    print(i)
