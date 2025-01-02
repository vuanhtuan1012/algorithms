# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2024-11-08 16:45:44
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-02 22:51:01

"""
Viết một hàm xác định xem một số nguyên dương đã cho có phải là số nguyên tố hay không.
"""


def is_prime(number: int) -> bool:
    """
    Returns True if the given number is prime otherwise False
    """
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def dry_tests():
    """
    Dry tests
    """
    test_cases = [(47, True), (4, False), (133, False), (0, False)]
    for number, ground_truth in test_cases:
        result = is_prime(number)
        print(f"is_prime({number}) = {result}: {result == ground_truth}")


if __name__ == "__main__":
    dry_tests()
