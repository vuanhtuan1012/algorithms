# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-03 22:46:28
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-03 22:58:27

"""
Cho một danh sách các phân số, hãy tìm chỉ số của phân số lớn nhất (đếm từ 0).
Giả định rằng không có các phân số bằng nhau trong tập đầu vào.

Ví dụ:
Với numerators = [5, 2, 5] và denominators = [6, 3, 4], thì kết quả
max_fraction(numerators, denominators) = 2
vì 5/4 là phân số lớn nhất, có chỉ số là 2.

Tại sao không khai báo kiểu biến số thực rồi so sánh trực tiếp luôn?
Thực tế là, máy tính không thể tính toán chính xác được những phân số không hữu hạn.
Nó sẽ làm tròn giá trị phân số đến 1 lượng chữ số thập phân nào đấy.
Và sẽ có rủi ro phần lẻ khi bạn tính toán, so sánh các phân số với nhau.
"""
from typing import List


def find_max_fraction_idx(numerators: List[int], denominators: List[int]) -> int:
    """
    Returns the index of the largest fraction
    """
    idx = 0
    for i, (numerator, denominator) in enumerate(zip(numerators, denominators)):
        if numerator * denominators[idx] > numerators[idx] * denominator:
            idx = i
    return idx


def dry_tests():
    """
    Dry tests
    """
    test_cases = [
        ([5, 2, 5], [6, 3, 4], 2),
        ([1, 2, 3, 10], [1, 3, 4, 11], 0),
        ([1, 2], [4, 3], 1),
    ]
    for numerators, denominators, ground_truth in test_cases:
        result = find_max_fraction_idx(numerators, denominators)
        print(
            f"max_fraction_idx({numerators}, {denominators}) = {result}"
            f": {result == ground_truth}"
        )


if __name__ == "__main__":
    dry_tests()
