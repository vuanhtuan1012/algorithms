# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-16 23:01:07
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-22 15:50:05

"""
Định nghĩa phép toán crossover của hai xâu có độ dài bằng nhau A và B như sau:
- Kết quả của phép toán này là một xâu result có độ dài bằng với hai xâu đầu vào.
- result[i] bằng A[i] hoặc B[i].

Cho một danh sách các xâu có độ dài bằng nhau inputArray và một xâu result,
hãy đếm xem có bao nhiêu cặp xâu trong mảng đã cho mà
kết quả của phép toán crossover cho ra kết quả là result.

Ví dụ:
Với inputArray = ["abc", "aaa", "aba", "bab"] và result = "bbb",
kết quả stringsCrossover(inputArray, result) = 2.
Có 2 cặp xâu kí tự thỏa mãn yêu cầu đề bài là:
- abc vs bab
- aba vs bab
"""

from typing import List


def is_crossover(first_string: str, second_string: str, result: str) -> bool:
    """
    Returns True if result is the result of crossover operator between two strings
    otherwise, return False
    """
    length = len(first_string)
    if length != len(second_string) or length != len(result):
        return False

    for i in range(length):
        if result[i] not in (first_string[i], second_string[i]):
            return False
    return True


def count_crossover(array: List[str], result: str) -> int:
    """
    Returns the number of pairs of strings in array for which
    the operation crossover on them results in result
    """
    no_strings = len(array)
    no_pairs = 0
    for i in range(no_strings - 1):
        first_string = array[i]
        for j in range(i + 1, no_strings):
            if is_crossover(first_string, array[j], result):
                no_pairs += 1
    return no_pairs


def dry_tests():
    """
    Dry tests
    """
    test_cases = [
        (["abc", "aaa", "aba", "bab"], "bbb", 2),
        (["aacccc", "bbcccc"], "abdddd", 0),
        (["a", "b", "c", "d", "e"], "c", 4),
        (["aa", "ab", "ba"], "bb", 1),
    ]
    for i, (array, result, ground_truth) in enumerate(test_cases):
        no_pairs = count_crossover(array, result)
        print(f"Test case {i + 1}: {no_pairs == ground_truth}")


if __name__ == "__main__":
    dry_tests()
