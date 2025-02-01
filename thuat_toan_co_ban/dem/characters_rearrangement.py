# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-31 23:54:22
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-02-01 19:41:46

"""
Cho hai xâu kí tự, hãy kiểm tra xem có tồn tại phương án
đổi chỗ các kí tự ở trong xâu thứ nhất để trở thành xâu thứ hai được hay không?

Ví dụ:
- charactersRearrangement("abcd", "cbad") = True
- charactersRearrangement("a", "b") = False
"""
from typing import Dict


def get_frequency(string: str) -> Dict[str, int]:
    """
    Returns frequency of letters in the given string
    """
    freq = {}
    for letter in string:
        freq[letter] = freq.get(letter, 0) + 1
    return freq


def is_permutable(first_string: str, second_string: str) -> bool:
    """
    Returns True if two strings are permutation, otherwise False
    """
    return get_frequency(first_string) == get_frequency(second_string)


def dry_tests():
    """
    Dry tests
    """
    test_cases = [
        ("aaad", "aaa", False),
        ("abcd", "cbad", True),
        ("a", "b", False),
        ("aaa", "aaaa", False),
        ("abcdef", "badcfe", True),
    ]
    for i, (first_string, second_string, ground_truth) in enumerate(
        test_cases, start=1
    ):
        result = is_permutable(first_string, second_string)
        print(f"Test case {i}: {result == ground_truth}")


if __name__ == "__main__":
    dry_tests()
