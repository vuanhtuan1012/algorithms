# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2024-11-08 17:53:45
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-02 22:09:08

"""
Chúng ta có một số nguyên dương n.
Mỗi một lần ta thay thế n bằng tổng các thừa số nguyên tố của nó
(ví dụ 12=2*2*3 thì 12 sẽ được thay thế bằng số 2+2+3=7)

Chúng ta áp dụng phép toán này vào số hiện tại cho đến khi
kết quả thu được giống vs số hiện tại.

Cho một số tự nhiên, hãy tìm kết quả cuối cùng của phép toán trên.
"""
from typing import List


def find_prime_factors(number: int) -> List[int]:
    """
    Returns the list of prime factors of the given number
    """
    i = 2
    prime_factors = []
    while number > 1:
        while number % i == 0:
            prime_factors.append(i)
            number = number // i
        i += 1

    return prime_factors


def find_factor_sum(number: int) -> int:
    """
    Returns the factor sum of the given number
    """
    prime_factors = find_prime_factors(number)
    while number != sum(prime_factors):
        number = sum(prime_factors)
        prime_factors = find_prime_factors(number)
    return number


def dry_tests():
    """
    Dry tests
    """
    test_cases = [(0, 0), (24, 5), (35, 7), (156, 5)]
    for number, ground_truth in test_cases:
        result = find_factor_sum(number)
        print(f"find_factor_sum({number}) = {result}: {result == ground_truth}")


if __name__ == "__main__":
    dry_tests()
