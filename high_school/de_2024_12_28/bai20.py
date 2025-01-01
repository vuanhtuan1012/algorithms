# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-01 07:04:12
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-01 07:45:09

"""
Bài 20

Chèn x vào phần tử thứ k của dãy số a có n phần tử.
Đưa ra số phần tử và dãy số a sau khi chèn.

Ví dụ:
inserarr.inp
6 4 8
4 6 5 9 3 7
inserarr.out
7
4 6 5 8 9 3 7
"""
from typing import List, Tuple


def doc_file(filename: str) -> Tuple[int, int, List[int]]:
    """
    Returns number, position, and the list of numbers read from the given file
    """
    number, position, array = 0, -1, []
    print(f"Doc file {filename}.")
    with open(filename, encoding="utf-8") as file_pointer:
        for i, line in enumerate(file_pointer):
            if i == 0:
                _, position, number = map(int, line.split())
            if i == 1:
                array = list(map(int, line.split()))
    return number, position, array


def chen_phan_tu(number: int, position: int, array: List[int]):
    """
    Insert the given number to the position (1-index) of the given list
    """
    position -= 1
    position = 0 if position < 0 else position
    position = len(array) if position > len(array) else position
    array.insert(position, number)


def ghi_file(array: List[int], filename: str):
    """
    Writes length and the given list to file
    """
    with open(filename, "w", encoding="utf-8") as file_pointer:
        file_pointer.write(f"{len(array)}\n")
        line = " ".join(str(number) for number in array)
        file_pointer.write(f"{line}\n")
    print(f"Ghi ket qua thanh cong vao file {filename}")


def main():
    """
    Main function
    """
    number, position, array = doc_file("data/inserarr.inp")
    chen_phan_tu(number, position, array)
    ghi_file(array, "data/inserarr.out")


if __name__ == "__main__":
    main()
