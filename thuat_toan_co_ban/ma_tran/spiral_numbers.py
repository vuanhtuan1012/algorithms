# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-02-10 23:00:35
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-02-12 15:52:20

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


def print_matrix(matrix: Matrix):
    """
    Prints the given matrix
    """
    size = len(matrix)
    length = len(str(size**2))
    for row in range(size):
        print(" ".join(map(lambda ele: str(ele).ljust(length), matrix[row])))


def dry_tests():
    """
    Dry tests
    """
    test_cases = [
        (3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),
        (
            5,
            [
                [1, 2, 3, 4, 5],
                [16, 17, 18, 19, 6],
                [15, 24, 25, 20, 7],
                [14, 23, 22, 21, 8],
                [13, 12, 11, 10, 9],
            ],
        ),
        (
            6,
            [
                [1, 2, 3, 4, 5, 6],
                [20, 21, 22, 23, 24, 7],
                [19, 32, 33, 34, 25, 8],
                [18, 31, 36, 35, 26, 9],
                [17, 30, 29, 28, 27, 10],
                [16, 15, 14, 13, 12, 11],
            ],
        ),
    ]

    for i, (number, ground_truth) in enumerate(test_cases, start=1):
        result = create_spiral_matrix(number)
        print(f"Test case {i}: number = {number}, result:")
        print_matrix(result)
        print(f"Test case {i}: {result == ground_truth}")


if __name__ == "__main__":
    dry_tests()
