# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-02-02 17:39:54
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-02-02 18:49:43

"""
Cho một ma trận chữ nhật chứa các chữ số (0-9).
Hãy tính số lượng các hình vuông 2x2 khác nhau tồn tại trong ma trận.

Ví dụ: với matrix = [
    [1, 2, 1],
    [2, 2, 2],
    [2, 2, 2],
    [1, 2, 3],
    [2, 2, 1]
]
thì kết quả differentSquares(matrix) = 6.
"""
from typing import List


def to_string(square: List[List[int]]) -> str:
    """
    Returns the string which represent the given square
    """
    return "\n".join(map(str, ("".join(map(str, row)) for row in square)))


def count_different_squares(matrix: List[List[int]]) -> int:
    """
    Returns number of different 2x2 squares in the given matrix
    """
    squares = set()
    no_rows = len(matrix)
    no_columns = len(matrix[0]) if no_rows > 0 else 0
    for i in range(no_rows - 1):
        for j in range(no_columns - 1):
            square = [matrix[i][j : j + 2], matrix[i + 1][j : j + 2]]
            str_square = to_string(square)
            squares.add(str_square)
    return len(squares)
