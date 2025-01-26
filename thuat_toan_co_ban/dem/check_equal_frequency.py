# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-26 23:23:53
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-26 23:56:06

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
    return all(frequencies[element] == standard for element in frequencies)


def dry_tests():
    """
    Dry tests
    """
    test_cases = [
        ([1, 2, 2, 1], True),
        ([1, 2, 2, 3, 1, 3, 1, 3], False)
    ]
