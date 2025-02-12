# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-02-10 23:00:35
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-02-12 11:28:08

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


def create_spiral_matrix(number: int) -> List[List[int]]:
    """
    Returns the spiral matrix of the given number
    """
    matrix = []
    for _ in range(number):
        matrix.append([0] * number)
    left = 0
    right = number - 1
    val = 1
    while val <= number**2:
        # left to right
        for col in range(left, right + 1):
            if val > number**2:
                return matrix
            matrix[left][col] = val
            val += 1
        # top down
        for row in range(left + 1, right + 1):
            if val > number**2:
                return matrix
            matrix[row][right] = val
            val += 1
        # right to left
        for col in range(right - 1, left - 1, -1):
            if val > number**2:
                return matrix
            matrix[right][col] = val
            val += 1
        # bottom up
        for row in range(right - 1, left, -1):
            if val > number**2:
                return matrix
            matrix[row][left] = val
            val += 1
        left += 1
        right -= 1
    return matrix
