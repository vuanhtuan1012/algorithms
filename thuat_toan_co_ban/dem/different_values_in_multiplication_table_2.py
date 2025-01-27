# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-25 23:38:47
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-28 06:23:36

"""
Cho một bảng có n hàng và m cột.
Mỗi một ô trong bảng ở hàng i và cột j chứa 1 số có giá trị
bằng i * j (chỉ số hàng và cột đều được đếm bắt đầu từ 1)
Cho trước n và m, hãy tìm số lượng các số nguyên khác nhau nằm trong bảng.

Ví dụ:
- differentValuesInMultiplicationTable2(3, 2) = 5
  vì có 5 giá trị khác nhau trong bảng là: 1, 2, 3, 4, 6
"""


def count_different_values(no_rows: int, no_cols: int) -> int:
    """
    Returns number of unique values in multiplication table
    """
    unique_values = set()
    no_unique_values = 0
    for i in range(1, no_rows + 1):
        for j in range(1, no_cols + 1):
            value = i * j
            if value not in unique_values:
                unique_values.add(value)
                no_unique_values += 1
    return no_unique_values


def dry_tests():
    """
    Dry tests
    """
    test_cases = [(3, 2, 5), (4, 4, 9)]
    for no_rows, no_cols, ground_truth in test_cases:
        result = count_different_values(no_rows, no_cols)
        print(
            f"count_different_values({no_rows}, {no_cols}) = {result}: {result == ground_truth}"
        )


if __name__ == "__main__":
    dry_tests()
