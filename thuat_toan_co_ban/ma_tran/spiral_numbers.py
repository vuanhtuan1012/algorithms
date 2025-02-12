# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-02-10 23:00:35
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-02-12 15:23:47

"""
Cho số nguyên dương n.
Hãy tạo ra ma trận vuông kích thước n*n chứa các số từ 1 tới n*n tăng dần
theo hình xoắn ốc, xuất phát từ ô trên trái và đi theo theo theo chiều kim đồng hồ.

Ví dụ:
spiralNumbers(3) = [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]
]
spiralNumbers(4) = [
    [ 1,  2,  3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10,  9,  8, 7]
]
"""
from typing import List

Matrix = List[List[List]]


def fill_matrix_border(
    lower_idx: int, upper_idx: int, matrix: Matrix, start_value: int
) -> int:
    """
    Returns the value after fill in the matrix border
    """
    value = start_value
    limit = len(matrix) ** 2

    # left to right
    for col in range(lower_idx, upper_idx + 1):
        if value > limit:
            return value
        matrix[lower_idx][col] = value
        value += 1

    # top down
    for row in range(lower_idx + 1, upper_idx + 1):
        if value > limit:
            return value
        matrix[row][upper_idx] = value
        value += 1

    # right to left
    for col in range(upper_idx - 1, lower_idx - 1, -1):
        if value > limit:
            return value
        matrix[upper_idx][col] = value
        value += 1

    # bottom up
    for row in range(upper_idx - 1, lower_idx, -1):
        if value > limit:
            return value
        matrix[row][lower_idx] = value
        value += 1
    return value


def create_spiral_matrix(number: int) -> Matrix:
    """
    Returns the spiral matrix of the given number
    """
    # initialize matrix
    matrix = []
    for _ in range(number):
        matrix.append([0] * number)

    # fill in the matrix
    lower_idx = 0  # lower index bound
    upper_idx = number - 1  # upper index bound
    value = 1
    while value <= number**2:
        # fill the matrix border from the outside in
        value = fill_matrix_border(lower_idx, upper_idx, matrix, value)
        lower_idx += 1
        upper_idx -= 1
    return matrix
