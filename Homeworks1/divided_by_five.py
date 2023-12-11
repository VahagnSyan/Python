"""
    Display numbers divisible by 5 from a list
"""


def test_divisible_by_five():
    nums = [10, 15, 20, 25, 30]
    assert divisible_by_five(nums) == [10, 15, 20, 25, 30], "Test case 1 failed"

    nums = []
    assert divisible_by_five(nums) == [], "Test case 2 failed"

    nums = [11, 17, 23, 31]
    assert divisible_by_five(nums) == [], "Test case 3 failed"

    nums = [8, 10, 12, 15, 18]
    assert divisible_by_five(nums) == [10, 15], "Test case 4 failed"

    print("All test cases passed")


def divisible_by_five(nums):
    result = []
    for num in nums:
        if num % 5 == 0:
            result.append(num)
    return result


test_divisible_by_five()
