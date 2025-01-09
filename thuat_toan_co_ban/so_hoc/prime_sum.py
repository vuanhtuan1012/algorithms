# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-07 23:48:42
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-09 17:59:44

"""
Cho số nguyên n, hãy tính tổng các số nguyên tố nhỏ hơn hoặc bằng n.

Bởi vì tổng các số nguyên tố nhỏ hơn hoặc bằng n có thể rất lớn,
nên hãy trả ra kết quả của tổng trên dưới dạng là số dư trong phép chia của tổng trên cho 22082018.

Ví dụ:
- Với n = 2 thì primeSum(n) = 2
- Với n = 3 thì primeSum(n) = 5
"""
from typing import List


def sieve_eratosthenes(number: int) -> List[int]:
    """
    Returns list of prime numbers which are less than or equal the given number
    """
    is_prime_numbers = [True for _ in range(number + 1)]
    is_prime_numbers[0] = is_prime_numbers[1] = False
    for i in range(2, number + 1):
        j = 2
        idx = i * j
        while idx <= number:
            if is_prime_numbers[idx]:
                is_prime_numbers[idx] = False
            j += 1
            idx = i * j
    return [element for element in range(number + 1) if is_prime_numbers[element]]


def get_prime_sum(number: int) -> int:
    """
    Returns the sum of prime numbers which are less than or equal the given number
    """
    return sum(sieve_eratosthenes(number))


def dry_tests():
    """
    Dry tests
    """
    test_cases = [(2, 2), (3, 5), (5, 10), (10000, 5736396)]
    for number, ground_truth in test_cases:
        result = get_prime_sum(number)
        print(f"get_prime_sum({number}) = {result}: {result == ground_truth}")


if __name__ == "__main__":
    dry_tests()
