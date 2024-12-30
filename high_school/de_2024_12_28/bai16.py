# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2024-12-30 20:28:28
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2024-12-30 21:04:24

"""
Bài 16

Cho dãy số a (m phần tử), dãy số b (n phần tử). Tìm giá trị a_i + b_j lớn nhất.

Ví dụ:
maxarr.inp
6 4
3 4 6 2 7 3
3 9 5 7

maxarr.out
16
"""
from typing import List


def doc_file(filename: str) -> List[List[int]]:
    """
    Returns the list of number lists in the given file
    """
    number_lists = []
    print(f"Doc file {filename}")
    with open(filename, encoding="utf-8") as file_pointer:
        for i, line in enumerate(file_pointer):
            if i >= 1:
                numbers = list(map(int, line.split()))
                number_lists.append(numbers)
    return number_lists


def tim_so_lon_nhat(numbers: List[int]) -> int:
    """
    Returns the largest number in the given list
    """
    largest_num = numbers[0]
    for num in numbers:
        if num > largest_num:
            largest_num = num
    return largest_num


def tim_tong_lon_nhat(number_lists: List[List[int]]) -> int:
    """
    Returns the largest total
    """
    largest_total = 0
    for numbers in number_lists:
        largest_total += tim_so_lon_nhat(numbers)
    return largest_total


def ghi_file(largest_total: int, filename: str):
    """
    Writes the largest total to the given file
    """
    with open(filename, "w", encoding="utf-8") as file_pointer:
        file_pointer.write(str(largest_total))
    print(f"Tong lon nhat duoc ghi vao file {filename}")


def main():
    """
    Main function
    """
    number_lists = doc_file("data/maxarr.inp")
    largest_total = tim_tong_lon_nhat(number_lists)
    ghi_file(largest_total, "data/maxarr.out")


if __name__ == "__main__":
    main()
