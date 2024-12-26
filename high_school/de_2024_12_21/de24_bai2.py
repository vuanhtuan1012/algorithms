# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2024-12-26 12:35:00
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2024-12-26 12:45:52

"""
Đề số 24 - Bài 2 - Trang 149

Giai thừa của một số n (kí hiệu n!) là tích các số tự nhiên từ 1 đến n
(n! = 1.2.3...n và qui ước 0! = 1).
Viết chương trình tính n! với n là số tự nhiên nhập từ bàn phím (n < 10).
"""


def tinh_giai_thua(n: int) -> int:
    """
    Returns the factorial of the given integer
    """
    giai_thua = 1
    for i in range(1, n + 1):
        giai_thua *= i
    return giai_thua


def main():
    """
    Main function
    """
    n = int(input("Nhap n = "))
    print(f"{n}! = {tinh_giai_thua(n)}")


if __name__ == "__main__":
    main()
