# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2024-12-25 13:12:59
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2024-12-27 11:07:32

"""
Đề số 1 - Bài 3 - Trang 7, 8

Viết chương trình nhập một xâu kí tự S chỉ gồm các chữ cái in thường và chữ số.
In ra màn hình:
- Số tự nhiên a sau khi xoá các chữ cái trong S.
- Xoá một số chữ số của a để được số tự nhiên b lớn nhất chia hết cho 5.
  Nếu không tìm được in ra KHONG.
- Số T là tổng các số có trong xâu S.

Ví dụ: với S = hsg8ngay21thang4nam2023 thì in ra kết quả:
a = 82142023
b = 821420
T = 2056
"""
from typing import Optional


def tim_so(string: str) -> str:
    """
    Returns number after removing letters in the given string
    """
    number = ""
    for element in string:
        if element.isdigit():
            number += element
    return number


def giai_cau_1(string: str):
    """
    Prints the number after removing letters in the given string
    """
    number = tim_so(string)
    if number:
        print(f"a = {number}")
    else:
        print("Khong co so trong chuoi!")


def tim_so_lon_nhat_chc_5(number: str) -> Optional[str]:
    """
    Returns the largest number divisible by 5
    by removing some digits from the given number
    """
    while number:
        if int(number) % 5 == 0:
            return number
        number = number[:-1]
    return None


def giai_cau_2(string: str):
    """
    Prints the largest number divisible by 5
    by removing letters and some digits form the given string
    """
    number = tim_so_lon_nhat_chc_5(tim_so(string))
    if number is None:
        print("KHONG")
    else:
        print(f"b = {number}")


def tim_tong(string: str) -> int:
    """
    Returns sum of numbers in the given string
    """
    tong = 0
    number = ""
    for element in string:
        if element.isdigit():
            number += element
        else:
            if number:
                tong += int(number)
                number = ""
    if number:
        tong += int(number)
    return tong


def giai_cau_3(string: str):
    """
    Prints sum of numbers in the given string
    """
    print(f"T = {tim_tong(string)}")


def dry_tests():
    """
    Dry tests
    """
    strings = [
        "hsg8ngay21thang4nam2023",
        "ngay8thang12",
        "ngay08thang12",
        "daylachuoikhongcoso",
        "daylachuoi0coso",
    ]
    for string in strings:
        print(f"\nS = {string}")
        giai_cau_1(string)
        giai_cau_2(string)
        giai_cau_3(string)


def main():
    """
    Main function
    """
    string = input("Nhap xau S: ")
    giai_cau_1(string)
    giai_cau_2(string)
    giai_cau_3(string)


if __name__ == "__main__":
    main()
