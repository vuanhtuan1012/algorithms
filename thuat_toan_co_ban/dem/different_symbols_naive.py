# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-28 06:28:36
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-28 06:35:23

"""
Cho xâu kí tự. Hãy đếm số lượng kí tự khác nhau trong xâu đó

Ví dụ: differentSymbolsNaive("cabca") = 3
"""


def count_unique_chars(sequence: str) -> int:
    """
    Returns number of unique chars in the given sequence
    """
    unique_chars = set()
    no_unique_chars = 0
    for char in sequence:
        if char not in unique_chars:
            unique_chars.add(char)
            no_unique_chars += 1
    return no_unique_chars


def dry_tests():
    """
    Dry tests
    """
    test_cases = [("cabca", 3), ("aba", 2), ("ccccccccccc", 1), ("bcaba", 3)]
    for sequence, ground_truth in test_cases:
        result = count_unique_chars(sequence)
        print(f"count_unique_chars({sequence}) = {result}: {result == ground_truth}")


if __name__ == "__main__":
    dry_tests()
