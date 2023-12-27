'''Function for return fibonachi number with recursion'''


def fibonachi_number(number):
    '''Returns the number th Fibonacci term'''

    if number in (1, 2):
        return 1
    return (fibonachi_number(number-1) + fibonachi_number(number-2))


print(fibonachi_number(50))
