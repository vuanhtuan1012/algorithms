# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2024-12-30 22:48:11
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2024-12-30 23:07:25

"""
Bài 17

Xoá phần tử thứ k của mảng a có n phần tử. Đưa ra số phần tử còn lại và mảng a sau khi xoá.

Ví dụ:
delarr.inp
6 4
5 7 3 4 6 9
delarr.out
5
5 7 3 6 9
"""
from typing import List, Tuple


def doc_file(filename: str) -> Tuple[int, List[int]]:
    """
    Returns the index and the list of numbers read from the given file
    """
    index, numbers = -1, []
    print(f"Doc file {filename}.")
    with open(filename, encoding="utf-8") as file_pointer:
        for i, line in enumerate(file_pointer):
            if i == 0:
                _, index = map(int, line.split())
            if i == 1:
                numbers = list(map(int, line.split()))
    return index, numbers


def xoa_phan_tu(index: int, numbers: List[int]):
    """
    Remove the element at a given position (1-index) of the given list
    """
    index -= 1
    if 0 <= index < len(numbers):
        numbers.pop(index)


def ghi_file(numbers: List[int], filename: str):
    """
    Writes length and numbers of the given list to file
    """
    with open(filename, "w", encoding="utf-8") as file_pointer:
        file_pointer.write(f"{len(numbers)}\n")
        line = " ".join(str(num) for num in numbers)
        file_pointer.write(f"{line}\n")
    print(f"Ghi ket qua thanh cong vao file {filename}")


def main():
    """
    Main function
    """
    index, numbers = doc_file("data/delarr.inp")
    xoa_phan_tu(index, numbers)
    ghi_file(numbers, "data/delarr.out")


if __name__ == "__main__":
    main()
