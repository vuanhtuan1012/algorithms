# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-13 22:44:57
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-13 22:56:34

"""
Xóa các khoảng trắng thừa (kí tự cách) trong xâu kí tự cho trước,
sao cho giữa các từ chỉ cách nhau bởi 1 khoảng trống.
Cũng không có khoảng trống ở đầu và cuối của xâu.

Ví dụ:
- formatString(" abc   a aa  a a ") = "abc a aa a a"

"""


def format_string(string: str) -> str:
    """
    Returns string formated
    """
    string_formated = ""
    for char in string:
        if char != " ":
            string_formated += char
            continue
        if string_formated and string_formated[-1] != " ":
            string_formated += char
    return string_formated.strip()


def dry_tests():
    """
    Dry tests
    """
    test_cases = [
        (" abc   a aa  a a ", "abc a aa a a"),
        ("abcd", "abcd"),
        ("        a           ", "a"),
    ]
    for string, ground_truth in test_cases:
        result = format_string(string)
        print(f"format_string({string}) = {result}: {result == ground_truth}")


if __name__ == "__main__":
    dry_tests()
