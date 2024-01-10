def filter(func, iterable):
    for item in iterable:
        if func(item):
            yield item

def is_even(num):
    return num % 2 == 0

def is_vowel(symbol):
    return symbol.lower() in 'aeiou'

text = "ejk vknkn fdvkd jwd,s sa;jbdas"
l = [1, 2, 3, 5, 6]

# Assertions
assert list(filter(is_even, l)) == [2, 6], "Answer must be [2, 6]"
assert list(filter(is_vowel, text)) == ['e', 'a', 'a'], "Answer must be ['e', 'a', 'a']"

l = [2.3, 2, 5, 6]
assert list(filter(is_even, l)) == [2, 6], "Answer must be [2, 6]"
