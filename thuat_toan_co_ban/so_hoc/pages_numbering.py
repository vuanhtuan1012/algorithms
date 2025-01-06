# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-06 23:15:51
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-06 23:53:25

"""
Cho biết số trang sách của 1 quyển sách.
Hãy tìm số lượng các chữ số dùng để đánh số trang của quyển sách đó.

Ví dụ:
- pagesNumbering(n) = 13.
13 chữ số được sử dụng là: 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0, 1, 1
"""


def get_number_of_digits_used(no_pages: int) -> int:
    """
    Returns the number of digits used to number the pages of a book
    """
    no_digits_used = 0
    degree = 1
    no_elements = 10**degree - 10 ** (degree - 1)
    while no_pages > no_elements:
        no_pages -= no_elements
        no_digits_used += no_elements * degree
        degree += 1
        no_elements = 10**degree - 10 ** (degree - 1)

    if no_pages > 0:
        no_digits_used += no_pages * degree
    return no_digits_used


def get_number_of_digits_used_v2(no_pages: int) -> int:
    """
    Returns the number of digits used to number the pages of a book
    """
    no_digits_used = 0
    degree = len(str(no_pages))
    for i in range(1, degree):
        no_elements = 10**i - 10 ** (i - 1)
        no_digits_used += no_elements * i
        no_pages -= no_elements

    if no_pages > 0:
        no_digits_used += no_pages * degree
    return no_digits_used


def dry_tests():
    """
    Dry tests
    """
    test_cases = [(11, 13), (1000, 2893), (13, 17), (1, 1)]
    print("Tests the first solution:")
    for no_pages, ground_truth in test_cases:
        result = get_number_of_digits_used(no_pages)
        print(
            f"- get_number_of_digits_used({no_pages}) = {result}: {result == ground_truth}"
        )
    print("Tests the second solution:")
    for no_pages, ground_truth in test_cases:
        result = get_number_of_digits_used_v2(no_pages)
        print(
            f"- get_number_of_digits_used_v2({no_pages}) = {result}: {result == ground_truth}"
        )


if __name__ == "__main__":
    dry_tests()
