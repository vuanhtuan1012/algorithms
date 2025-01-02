# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-02 22:18:41
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-02 22:53:56

"""
GCPD (Greatest Common Prime Divisor) được định nghĩa là
số nguyên tố lớn nhất là ước của các số nguyên dương cho trước.
Nhiệm vụ của bạn là tìm GCPD của hai số nguyên a và b.

Ví dụ:
- greatestCommonPrimeDivisor(12, 18) = 3
- greatestCommonPrimeDivisor(12, 13) = -1
"""
from typing import List


def get_sieve_eratosthenes(number: int) -> List[bool]:
    """
    Returns the sieve of Eratosthenes of the given number
    """
    sieve = [True for _ in range(number + 1)]
    sieve[0] = sieve[1] = False
    for i in range(2, int(number**0.5) + 1):
        # i isn't a prime
        if not sieve[i]:
            continue

        # i is a prime
        for j in range(2 * i, number + 1, i):
            sieve[j] = False
    return sieve


def find_greatest_common_prime_divisor(first_num: int, second_num: int) -> int:
    """
    Returns the greatest common prime divisor of two given numbers
    Returns -1 if not found
    """
    min_num = min(first_num, second_num)
    sieve = get_sieve_eratosthenes(min_num)
    for i in range(min_num, 1, -1):
        if sieve[i] and first_num % i == 0 and second_num % i == 0:
            return i
    return -1


def dry_tests():
    """
    Dry tests
    """
    test_cases = [(12, 18, 3), (12, 13, -1), (2, 3, -1), (100, 140, 5)]
    for first_num, second_num, ground_truth in test_cases:
        result = find_greatest_common_prime_divisor(first_num, second_num)
        print(
            f"greatest_common_prime_divisor({first_num}, {second_num}) = "
            f"{result}: {result == ground_truth}"
        )


if __name__ == "__main__":
    dry_tests()
