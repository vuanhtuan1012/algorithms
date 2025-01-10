# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-10 23:19:15
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-10 23:36:45

"""
Cho số tự nhiên n.
Hãy tính số chữ số 0 tận cùng của n!

Ví dụ:
- numberZeroDigits(5) = 1 vì 5! = 120
"""


def get_no_zero_digits(number: int) -> int:
    """
    Returns the number of trailing zeroes in the factorial of a given number
    """
    no_zeros = 0
    power_of_5 = 5
    while power_of_5 <= number:
        no_zeros += number // power_of_5
        power_of_5 *= 5
    return no_zeros


def dry_tests():
    """
    Dry tests
    """
    test_cases = [(5, 1), (10, 2), (100, 24), (5000, 1249), (1, 0)]
    for number, ground_truth in test_cases:
        result = get_no_zero_digits(number)
        print(f"get_no_zero_digits({number}) = {result}: {result == ground_truth}")


if __name__ == "__main__":
    dry_tests()
