# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2024-11-08 16:45:44
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-02 22:03:32

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
    numbers = [47, 4, 133, 0]
    for number in numbers:
        print(f"is_prime({number}) = {is_prime(number)}")


if __name__ == "__main__":
    dry_tests()
