# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-21 17:15:12
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-24 16:38:30

"""
Cho hai xâu kí tự, tìm số lượng kí tự chung giữa chúng.

Ví dụ:
- commonCharacterCount("aabcc", "adcaa") = 3 vì chúng có chung 2 kí tự "a" và 1 kí tự "c"
"""

from typing import Dict


def get_frequency(sequence: str) -> Dict[str, int]:
    """
    Returns frequency of letters in sequence
    """
    sequence = sequence.lower()
    freq = {}
    for letter in sequence:
        freq[letter] = freq.get(letter, 0) + 1
    return freq


def count_common_characters(sequence_1: str, sequence_2: str) -> int:
    """
    Returns the number of common characters between two given sequences
    """

    freq_1 = get_frequency(sequence_1)
    freq_2 = get_frequency(sequence_2)
    no_common_chars = 0
    for code in range(ord("a"), ord("z") + 1):
        letter = chr(code)
        no_common_chars += min(freq_1.get(letter, 0), freq_2.get(letter, 0))
    return no_common_chars


def dry_tests():
    """
    Dry tests
    """
    test_cases = [("abca", "xyzbac", 3), ("aabcc", "adcaa", 3), ("zzzz", "zzzzzzz", 4)]
    for i, (sequence_1, sequence_2, ground_truth) in enumerate(test_cases, start=1):
        result = count_common_characters(sequence_1, sequence_2)
        print(f"Test case {i}: {result == ground_truth}")


if __name__ == "__main__":
    dry_tests()
