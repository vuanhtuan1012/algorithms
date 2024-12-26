# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2024-12-25 15:17:14
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2024-12-26 06:09:56

"""
Đề số 2 - Bài 3 - Trang 16, 17

Viết chương trình nhập một xâu kí tự S gồm các chữ cái in thường, chữ số và kí tự trống (dấu cách).
In ra màn hình:
- Tổng các chữ số có trong xâu S
- Xâu S1 sau khi xoá các kí tự số trong S
- Xâu S2 sau khi xoá các kí tự liên tiếp giống nhau trong S1, chỉ giữ lại 1 kí tự.

Ví dụ: Với S = 5trrraann thhhhiii45 ttthannh ta64mmm, thì in ra kết quả:
- Tong cac chu so la: 24
- S1 = trrraann thhhhiii ttthannh tammm
- S2 = tran thi thanh tam
"""


def tim_tong_cac_cs(string: str) -> int:
    """
    Returns the sum of digits in the given string
    """
    tong = 0
    for element in string:
        if element.isdigit():
            tong += int(element)
    return tong


def xoa_ki_tu_so(string: str) -> str:
    """
    Returns string after removing digits in the given string
    """
    string_no_digits = ""
    for element in string:
        if not element.isdigit():
            string_no_digits += element
    return string_no_digits


def xoa_ki_tu_giong_nhau(string: str) -> str:
    """
    Returns string after removing consecutive identical characters in the given string
    """
    string_cleaned = ""
    for element in string:
        if not string_cleaned:
            string_cleaned += element
        elif string_cleaned[-1] != element:
            string_cleaned += element
    return string_cleaned


def dry_test():
    """
    Dry test
    """
    string = "5trrraann thhhhiii45 ttthannh ta64mmm"
    print(f"Tong cac chu so la: {tim_tong_cac_cs(string)}")
    print(f"S1 = {xoa_ki_tu_so(string)}")
    print(f"S2 = {xoa_ki_tu_giong_nhau(xoa_ki_tu_so(string))}")


def main():
    """
    Main function
    """
    string = input("Nhap xau S: ")
    print(f"Tong cac chu so la: {tim_tong_cac_cs(string)}")
    print(f"S1 = {xoa_ki_tu_so(string)}")
    print(f"S2 = {xoa_ki_tu_giong_nhau(xoa_ki_tu_so(string))}")


if __name__ == "__main__":
    main()
