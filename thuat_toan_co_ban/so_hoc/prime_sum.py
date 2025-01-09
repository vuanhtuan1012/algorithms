# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-07 23:48:42
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-09 22:14:17

"""
Cho số nguyên n, hãy tính tổng các số nguyên tố nhỏ hơn hoặc bằng n.

Bởi vì tổng các số nguyên tố nhỏ hơn hoặc bằng n có thể rất lớn,
nên hãy trả ra kết quả của tổng trên dưới dạng là số dư trong phép chia của tổng trên cho 22082018.

Ví dụ:
- Với n = 2 thì primeSum(n) = 2
- Với n = 3 thì primeSum(n) = 5
"""
from typing import List


# declare constants
MOD = 22082018


def get_sieve_eratosthenes(number: int) -> List[int]:
    """
    Returns the sieve Eratosthenes util the given number
    """
    sieve = list(range(number + 1))
    sieve[1] = 0
    for i in range(2, int(number**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, number + 1, i):
                sieve[j] = 0
    return sieve


def get_prime_sum(number: int) -> int:
    """
    Returns the sum of prime numbers which are less than or equal the given number
    """
    total = 0
    sieve = get_sieve_eratosthenes(number)
    for element in sieve:
        total = (total + element % MOD) % MOD
    return total


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
