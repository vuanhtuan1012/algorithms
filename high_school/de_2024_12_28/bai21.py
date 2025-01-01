# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-01 09:08:17
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-01 11:13:35

"""
Bài 21

Đếm số lần xuất hiện của mỗi phần tử trong dãy số.

Ví dụ:
xuathien.inp
6
3 5 3 6 5 7
xuathien.out
3 2
5 2
6 1
7 1
"""
from typing import Dict, List


def doc_file(filename: str) -> List[int]:
    """
    Returns the list of numbers read from the second line of given file
    """
    numbers = []
    print(f"Doc file {filename}.")
    with open(filename, encoding="utf-8") as file_pointer:
        for i, line in enumerate(file_pointer):
            if i != 1:  # read only the second line
                continue
            numbers = list(map(int, line.split()))
    return numbers


def dem_so_lan_xuat_hien(numbers: List[int]) -> Dict[int, int]:
    """
    Returns the frequencies of numbers in the given list.
    """
    frequencies = {}
    for number in numbers:
        frequencies[number] = frequencies.get(number, 0) + 1
    return frequencies


def ghi_file(frequencies: Dict[int, int], filename: str):
    """
    Writes the given list of numbers into the given file
    """
    with open(filename, "w", encoding="utf-8") as file_pointer:
        for number, freq in frequencies.items():
            file_pointer.write(f"{number} {freq}\n")
    print(f"So lan xuat hien cua cac so duoc ghi vao file {filename}")


def main():
    """
    Main function
    """
    numbers = doc_file("data/xuathien.inp")
    frequencies = dem_so_lan_xuat_hien(numbers)
    ghi_file(frequencies, "data/xuathien.out")


if __name__ == "__main__":
    main()
