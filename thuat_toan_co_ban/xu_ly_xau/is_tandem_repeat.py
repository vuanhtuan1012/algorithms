# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-13 23:01:38
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-13 23:10:54

"""
Cho một xâu kí tự s
Hãy kiểm tra xem xâu s có thể tạo ra bằng cách ghép một xâu vào chính nó hay không?

Ví dụ:
- isTandemRepeat("tandemtandem") = True vì tandem x 2 = tandemtandem
- isTandemRepeat("qqq") = False vì q x 2 != qqq
- isTandemRepeat("2w2ww") = False vì 2w x 2 != 2w2ww
"""


def is_tandem_repeat(string: str) -> bool:
    """
    Returns True if the given string is tandem repeat, otherwise False
    """
    mid_idx = len(string) // 2
    return string == string[:mid_idx] * 2


def dry_tests():
    """
    Dry tests
    """
    test_cases = [
        ("tandemtandem", True),
        ("qqq", False),
        ("2w2ww", False),
        ("hophey", False),
        ("viet", False),
        ("namnam", True),
        ("1111", True),
    ]
    for string, ground_truth in test_cases:
        result = is_tandem_repeat(string)
        print(f"is_tandem_repeat({string}) = {result}: {result == ground_truth}")


if __name__ == "__main__":
    dry_tests()
