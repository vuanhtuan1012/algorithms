# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-02-01 23:43:21
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-02-01 23:49:00

"""
Một pangram là một câu mà mỗi kí tự chữ cái (a-z) được sử dụng ít nhất một lần.
Cho một xâu kí tự, kiểm tra xem nó có phải là một pangram hay không?

Ví dụ:
- isPangram("The quick brown fox jumps over the lazy dog.") = True
- isPangram("abcdefghijklmnopqrstuvwxya") = False
"""


def is_pangram(sentence: str) -> bool:
    """
    Returns True if the given sentence is pangram, otherwise False
    """
    for code in range(ord("a"), ord("z") + 1):
        letter = chr(code)
        if letter not in sentence:
            return False
    return True
