# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-13 22:31:39
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-13 22:40:54

"""
Một xâu được gọi là palindrome nếu viết xuôi hay viết ngược xâu đó đều cho ra kết quả giống nhau
Cho một xâu kí tự, kiểm tra nó có phải xâu palindrome không.

Ví dụ:
- checkPalindrome("aabaa") = True
- checkPalindrome("abac") = False
- checkPalindrome("a") = True
"""


def is_palindrome(string: str) -> bool:
    """
    Returns True if given string is palindrome, otherwise False
    """
    reversed_string = string[::-1]
    return string == reversed_string


def dry_tests():
    """
    Dry tests
    """
    test_cases = [
        ("aabaa", True),
        ("abac", False),
        ("a", True),
        ("az", False),
        ("abba", True),
    ]
    for string, ground_truth in test_cases:
        result = is_palindrome(string)
        print(f"is_palindrome({string}) = {result}: {result == ground_truth}")


if __name__ == "__main__":
    dry_tests()
