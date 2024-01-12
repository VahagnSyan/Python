def my_repeat(obj, count):
    for i in range(count):
        yield obj


o = "qwerty"
a = my_repeat(o, 5)
for i in a:
    print(i)
