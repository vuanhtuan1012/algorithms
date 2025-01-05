# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-04 23:33:27
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-05 21:38:10

"""
Cho trước số tự nhiên number
Hãy tìm số nguyên dương nhỏ nhất (lớn hơn 0) mà tích các chữ số của số đó bằng number.
Nếu không có số thỏa mãn, trả ra -1.

Ví dụ:
- digitsProduct(12) = 26
- digitsProduct(19) = -1
- digitsProduct(108) = 269

Giải thích:
108 = 9 * 6 * 2
    = 9 * 4 * 3
    = 3 * 3 * 3 * 2 * 2
=> kết quả: 269 vì:
- (9, 6, 2) và (9, 4, 3) tối ưu về số chữ số.
- (9, 6, 2) tối ưu hơn (9, 4, 3) vì lấy 2 tốt hơn 3 khi làm chữ số đầu tiên.
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
    # edge cases
    if number == 0:
        return 10
    if number == 1:
        return 1

    # regular case
    digits_product = 0
    for i in range(9, 1, -1):
        while number % i == 0:
            # add i to the last
            digits_product = digits_product * 10 + i
            number //= i
    return reverse_digits(digits_product) if number == 1 else -1


def find_digits_product_v2(number: int) -> int:
    """
    Returns the smallest positive number such that
    the product of its digits equals the given number.
    """
    # edge cases
    if number == 0:
        return 10
    if number == 1:
        return 1

    # regular case
    digits_product = ""
    for i in range(9, 1, -1):
        while number % i == 0:
            # add i to the first
            digits_product = str(i) + digits_product
            number //= i
    return int(digits_product) if number == 1 else -1


def dry_tests():
    """
    Dry tests
    """
    test_cases = [(12, 26), (19, -1), (450, 2559), (0, 10), (13, -1), (108, 269)]
    print("Tests on version 1:")
    for number, ground_truth in test_cases:
        result = find_digits_product(number)
        print(f"- find_digits_product({number}) = {result}: {result == ground_truth}")
    print("Tests on version 2:")
    for number, ground_truth in test_cases:
        result = find_digits_product_v2(number)
        print(
            f"- find_digits_product_v2({number}) = {result}: {result == ground_truth}"
        )


if __name__ == "__main__":
    dry_tests()
