"""
    Get nth element of fibonacci sequence.
"""


def nth_from_fibonacci(nth_number: int) -> int:
    """
    Function returns nth element from fibonacci sequence.

    @params: n: integer (n >= 0)

    @return: int
    """

    if nth_number <= 2:
        return 1

    def calculate_fibonacci_seq(
        first_number: int, current_sum: int, current_n: int, nth_number: int
    ) -> int:
        """
        Recursive helper function for fibonacci sequence calculation.

        @return: int
        """

        if nth_number == current_n:
            return current_sum

        return calculate_fibonacci_seq(
            current_sum, first_number + current_sum, current_n + 1, nth_number
        )

    return calculate_fibonacci_seq(1, 1, 2, nth_number)


input_nth_number = int(input("Enter the nth number of fibonacci sequence: "))


print(nth_from_fibonacci(input_nth_number))
