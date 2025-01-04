# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-04 23:33:27
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-04 23:47:21

"""
Cho trước số tự nhiên number
Hãy tìm số nguyên dương nhỏ nhất (lớn hơn 0) mà tích các chữ số của số đó bằng number.
Nếu không có số thỏa mãn, trả ra -1.

Ví dụ:
- digitsProduct(12) = 26
- digitsProduct(19) = -1
"""


def reverse_digits(number: int) -> int:
    """
    Returns a number with the digits in reverse order of the given number.
    """
    return int(str(number)[::-1])


def find_digits_product(number: int) -> int:
    """
    Returns the smallest positive number such that
    the product of its digits equals the given number.
    """
    if number == 0:
        return 10
    if number == 1:
        return 1

    digits_product = 0
    for i in range(9, 1, -1):
        while number % i == 0:
            digits_product = digits_product * 10 + i
            number //= i
    return reverse_digits(digits_product) if number == 1 else -1


def dry_tests():
    """
    Dry tests
    """
    test_cases = [(12, 26), (19, -1), (450, 2559), (0, 10), (13, -1), (108, 269)]
    for number, ground_truth in test_cases:
        result = find_digits_product(number)
        print(f"find_digits_product({number}) = {result}: {result == ground_truth}")


if __name__ == "__main__":
    dry_tests()
