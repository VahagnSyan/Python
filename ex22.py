def filter(func, iterable):
    for item in iterable:
        if func(item):
            yield item

def is_even(num):
    return num % 2 == 0

def is_vowel(symbol):
    return symbol.lower() in 'aeiou'

text = 'ejk vknkn fdvkd jwd,s sa;jbdas'
result = list(filter(is_vowel, text))
print(f"for text")
print(result)
print()

l = [1, 2, 3, 5, 6]
result = list(filter(is_even, l))
print(f"for number")
print(result)
