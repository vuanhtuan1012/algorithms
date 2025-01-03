# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-03 23:02:21
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-03 23:47:35

"""
Tìm chữ số khác không cuối cùng của n! (giai thừa)

Ví dụ:
- last_digit_diff_zero(5) = 2 vì 5! = 120
- last_digit_diff_zero(6) = 2 vì 6! = 720
- last_digit_diff_zero(10) = 2 vì 5! = 3628800
"""


def find_last_non_zero_digit(number: int) -> int:
    """
    Returns the last non-zero digit of the factorial of given number
    """
    product = 1

    # remove trailing zeros
    for i in range(2, number + 1):
        product *= i

        # remove trailing zeros
        while product % 10 == 0:
            product //= 10

        # prevent product from becoming too large
        product %= 100

    # post cleanup
    if product % 10 == 0:
        product //= 10
    return product % 10


def dry_tests():
    """
    Dry tests
    """
    test_cases = [(5, 2), (6, 2), (10, 8), (1, 1), (2, 2), (4, 4), (20, 4)]
    for number, ground_truth in test_cases:
        result = find_last_non_zero_digit(number)
        print(f"last_non_zero_digit({number}) = {result}: {result == ground_truth}")


if __name__ == "__main__":
    dry_tests()
