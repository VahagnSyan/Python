# def my_repet(iterable, n):
#     for i in range(n):
#         for element in iterable:
#             yield element
            
# l = 'ani'
# print(list(my_repet(l, 5)))
def my_repet(iterable, n):
    for _ in range(n):
        yield iterable

l = 'ani'
print(list(my_repet(l, 5)))
