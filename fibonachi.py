'''Function for return fibonachi number with loop'''


def fibonachi_number(number):
    '''Returns the number th Fibonacci term'''

    if number in (1, 2):
        return 1
    num_1 = 1
    num_2 = 1
    result = 0
    for _ in range(number-2):
        result = num_1 + num_2
        num_1 = num_2
        num_2 = result
    return result


print(fibonachi_number(1500))
