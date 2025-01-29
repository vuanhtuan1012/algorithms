# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-29 23:47:44
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-30 06:54:21

"""
Cho một xâu kí tự, tìm số lượng xâu con khác nhau của xâu đó (không tính xâu rỗng).

Ví dụ:
- differentSubstringsTrie("abac") = 9
  9 xâu con khác nhau của xâu đầu vào là:
  "a", "b", "c", "ab", "ac", "ba", "aba", "bac", "abac"
"""


def count_unique_substrings(string: str) -> int:
    """
    Returns number of substrings
    """
    unique_substrings = set()
    length = len(string)
    for i in range(length):
        for j in range(i + 1, length + 1):
            unique_substrings.add(string[i:j])
    return len(unique_substrings)


def dry_tests():
    """
    Dry tests
    """
    test_cases = [("abac", 9), ("abacaba", 21)]
    for i, (string, ground_truth) in enumerate(test_cases, start=1):
        result = count_unique_substrings(string)
        print(f"Test case {i}: {result == ground_truth}")


if __name__ == "__main__":
    dry_tests()
