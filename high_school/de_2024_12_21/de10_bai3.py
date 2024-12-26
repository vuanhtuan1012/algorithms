# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2024-12-25 16:03:14
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2024-12-26 09:05:50

"""
Đề số 10 - Bài 3 - Trang 66, 67

Viết chương trình nhập n số nguyên từ bàn phím (n > 2). In ra màn hình:
- Số nguyên dương nhỏ nhất.
- Số nguyên âm lớn nhất.
- Các số xuất hiện hơn một lần và số lần xuất hiện của số đó.

Ví dụ: với n = 7 và các số được nhập là: 5, -3, 2, 5, -3, -1, 5
thì in ra kết quả:
- So nguyen duong nho nhat la 2.
- So nguyen am lon nhat la -1.
- So 5 xuat hien 3 lan.
- So -3 xuat hien 2 lan.
"""
from typing import Dict, List


def nhap_day_so() -> List[int]:
    """
    Returns list of numbers entered from keyboard
    """
    so_so_nguyen = int(input("n = "))
    array = []
    for i in range(so_so_nguyen):
        array.append(int(input(f"Nhập số thứ {i+1}: ")))
    return array


def tim_so_duong_nn(array: List[int]) -> int:
    """
    Returns the smallest positive integer in the given list
    """
    so_duong_nn = 0
    for number in array:
        if so_duong_nn == 0 and number > 0:
            so_duong_nn = number
        if 0 < number < so_duong_nn:
            so_duong_nn = number
    return so_duong_nn


def giai_cau_1(array: List[int]):
    """
    Prints the smallest positive integer in the given list
    """
    so_duong_nn = tim_so_duong_nn(array)
    if so_duong_nn == 0:
        print("- Khong co so nguyen duong trong day!")
    else:
        print(f"- So nguyen duong nho nhat la {so_duong_nn}.")


def tim_so_am_ln(array: List[int]) -> int:
    """
    Returns the largest negative integer in the given list
    """
    so_am_ln = 0
    for number in array:
        if so_am_ln == 0 and number < 0:
            so_am_ln = number
        if 0 > number > so_am_ln:
            so_am_ln = number
    return so_am_ln


def giai_cau_2(array: List[int]):
    """
    Prints the largest negative integer in the given list
    """
    so_am_ln = tim_so_am_ln(array)
    if so_am_ln == 0:
        print("- Khong co so nguyen am trong day!")
    else:
        print(f"- So nguyen am lon nhat la {so_am_ln}.")


def tim_tan_so(array: List[int]) -> Dict[int, int]:
    """
    Returns frequencies of numbers in the given list
    """
    tan_so = {}
    for number in array:
        tan_so[number] = tan_so.get(number, 0) + 1
    return tan_so


def giai_cau_3(array: List[int]):
    """
    Prints number and its frequency in the given list
    if its frequency is larger than 1.
    """
    tan_so = tim_tan_so(array)
    for number, freq in tan_so.items():
        if freq > 1:
            print(f"- So {number} xuat hien {freq} lan.")


def dry_test():
    """
    Dry test
    """
    array = [5, -3, 2, 5, -3, -1, 5]
    print("Day so:", ", ".join(str(ele) for ele in array))
    giai_cau_1(array)
    giai_cau_2(array)
    giai_cau_3(array)


def main():
    """
    Main function
    """
    array = nhap_day_so()
    giai_cau_1(array)
    giai_cau_2(array)
    giai_cau_3(array)


if __name__ == "__main__":
    main()
