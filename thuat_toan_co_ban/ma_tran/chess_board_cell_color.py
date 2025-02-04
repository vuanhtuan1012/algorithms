# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-02-03 11:18:42
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-02-04 15:45:52

"""
Cho địa chỉ hai ô trên bàn cờ vua tiêu chuẩn, hãy kiểm tra chúng cùng màu hay khác màu.

Ví dụ:
- chessBoardCellColor("A1", "C3") = True
- chessBoardCellColor("A1", "H3") = False
"""

from typing import Tuple


def get_indexes(cell: str) -> Tuple[int, int]:
    """
    Returns column index and row index of the given cell
    """
    return ord(cell[0].upper()), int(cell[1])


def is_same_color(first_cell: str, second_cell: str) -> bool:
    """
    Returns True if two given cell are the same color, otherwise False
    """
    manhattan_distance = sum(
        get_indexes(first_cell)[i] - get_indexes(second_cell)[i] for i in range(2)
    )
    return manhattan_distance % 2 == 0


def dry_tests():
    """
    Dry tests
    """
    test_cases = [
        ("A1", "C3", True),
        ("A1", "H3", False),
        ("A1", "A2", False),
        ("A1", "B2", True),
        ("B3", "H8", False),
    ]
    for i, (first_cell, second_cell, ground_truth) in enumerate(test_cases, start=1):
        result = is_same_color(first_cell, second_cell)
        print(f"Test case {i}: {result == ground_truth}")


if __name__ == "__main__":
    dry_tests()
