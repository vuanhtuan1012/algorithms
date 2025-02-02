# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-02-02 17:39:54
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-02-02 19:02:33

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


def build_square(
    row_idx: int, col_idx: int, matrix: List[List[int]], size: int
) -> List[List[int]]:
    """
    Returns the squre of given size in given matrix
    starting from the coordinator (row_index, col_index)
    """
    square = []
    for i in range(size):
        row = matrix[row_idx + i][col_idx : col_idx + size]
        square.append(row)
    return square


def count_different_squares(matrix: List[List[int]], size: int = 2) -> int:
    """
    Returns number of different squares of given size in the given matrix
    """
    squares = set()
    no_rows = len(matrix)
    no_columns = len(matrix[0]) if no_rows > 0 else 0
    for i in range(no_rows + 1 - size):
        for j in range(no_columns + 1 - size):
            square = build_square(i, j, matrix, size)
            str_square = to_string(square)
            squares.add(str_square)
    return len(squares)


def dry_tests():
    """
    Dry tests
    """
    test_cases = [
        ([[1, 2, 1], [2, 2, 2], [2, 2, 2], [1, 2, 3], [2, 2, 1]], 6),
        (
            [
                [9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9],
            ],
            1,
        ),
        ([[3]], 0),
    ]
    for i, (matrix, ground_truth) in enumerate(test_cases, start=1):
        result = count_different_squares(matrix)
        print(f"Test case {i}: {result == ground_truth}")


if __name__ == "__main__":
    dry_tests()
