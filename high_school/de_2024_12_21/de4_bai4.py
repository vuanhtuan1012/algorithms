# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2024-12-25 15:52:23
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2024-12-27 10:10:47

"""
Đề số 4 - Bài 4 - Trang 31

Viết chương trình nhập một số nguyên dương từ bàn phím (10 < n < 10^9).
In ra màn hình dãy các số nguyên dương có tổng các bình phương của chúng bằng n
và có số số hạng ít nhất. Nếu có nhiều lựa chọn thì chọn phương án có chứa số hạng lớn nhất.

Ví dụ: với n = 60 thì in ra màn hình:
Day can tim la: 7 3 1 1

Giải thích: 60 = 5^2 + 4^2 + 3^2 + 3^2 + 1^2
               = 6^2 + 4^2 + 2^2 + 2^2
               = 7^2 + 3^2 + 1^2 + 1^2
               = ...
Chọn phương án 7^2 + 3^2 + 1^2 + 1^2 vì có ít số hạng nhất và có chứa số hạng lớn nhất 7^2.
"""
from typing import List


def tim_tong_binh_phuong(number: int) -> List[int]:
    """
    Returns a list of numbers
    whose sum of the squares of its elements equals the given number
    """
    elements = []
    while number != 0:
        element = int(number**0.5)
        elements.append(element)
        number -= element**2
    return elements


def list_to_str(elements: List[int]) -> str:
    """
    Returns string containing all elements of the given list
    """
    return " ".join(str(element) for element in elements)


def dry_test():
    """
    Dry test
    """
    number = 60
    elements = tim_tong_binh_phuong(number)
    print(f"Day can tim la: {list_to_str(elements)}")


def main():
    """
    Main function
    """
    number = int(input("n = "))
    elements = tim_tong_binh_phuong(number)
    print(f"Day can tim la: {list_to_str(elements)}")


if __name__ == "__main__":
    main()
