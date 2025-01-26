# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-26 23:23:53
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-27 00:10:57

"""
Cho một mảng số nguyên
Hãy kiểm tra xem tần số xuất hiện của tất cả các số nguyên trong mảng
có bằng nhau hay không

Ví dụ:
- checkEqualFrequency([1, 2, 2, 1]) = true
- checkEqualFrequency([1, 2, 2, 3, 1, 3, 1, 3]) = false
"""
from typing import List, Dict


def get_frequencies(array: List[int]) -> Dict[int, int]:
    """
    Returns frequencies of elements in the given array
    """
    frequencies = {}
    for element in array:
        frequencies[element] = frequencies.get(element, 0) + 1
    return frequencies


def check_equal_frequency(array: List) -> bool:
    """
    Returns True if frequencies of elements in the given array equal
    otherwise False
    """
    frequencies = get_frequencies(array)
    standard = frequencies[array[0]]
    return all(freq == standard for _, freq in frequencies.items())


def dry_tests():
    """
    Dry tests
    """
    test_cases = [
        ([1, 2, 2, 1], True),
        ([1, 2, 2, 3, 1, 3, 1, 3], False),
        ([239], True),
        ([239, 240, 241], True),
        ([34, 23, 33, 23], False),
        ([1, 1, 1, 1, 1], True),
    ]

    for i, (array, ground_truth) in enumerate(test_cases, start=1):
        result = check_equal_frequency(array)
        print(f"Test case {i}: {result == ground_truth}")


if __name__ == "__main__":
    dry_tests()
