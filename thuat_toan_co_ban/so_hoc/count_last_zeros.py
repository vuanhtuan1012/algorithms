# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-04 12:57:32
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-04 13:09:41

"""
Tìm số chữ số không cuối cùng của n! (giai thừa)

Ví dụ:
- count_last_zeros(5) = 1 vì 5! = 120
- count_last_zeros(10) = 2 vì 5! = 3628800
"""


def count_last_zeros(number: int) -> int:
    """
    Returns the number of last zeros of the factorial of given number
    """
    num_zeros = 0
    product = 1
    for i in range(2, number + 1):
        product *= i

        # count number of last zeros
        while product % 10 == 0:
            product //= 10
            num_zeros += 1

        # prevent product from becoming too large
        product %= 100

    # post counting
    if product % 10 == 0:
        num_zeros += 1

    return num_zeros


def dry_tests():
    """
    Dry tests
    """
    test_cases = [(5, 1), (10, 2)]
    for number, ground_truth in test_cases:
        result = count_last_zeros(number)
        print(f"count_last_zeros({number}) = {result}: {result == ground_truth}")


if __name__ == "__main__":
    dry_tests()
