# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-01 16:51:56
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-01 17:40:18

"""
Bài 27

Liệt kê các số chính phương có trong dãy số a. Nếu không có ghi -1.

Ví dụ:
socp.inp
10
3 4 7 5 9 3 16 21 36 8
socp.out
4 9 16 36
"""
from typing import List


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


def tim_day_so_cp(numbers: List[int]) -> List[int]:
    """
    Returns the array of square numbers from the given array
    """
    square_numbers = []
    for number in numbers:
        squared_root = int(number**0.5)
        if squared_root**2 == number:
            square_numbers.append(number)
    return square_numbers


def ghi_file(numbers: List[int], filename: str):
    """
    Writes the elements of the given list to file
    """
    with open(filename, "w", encoding="utf-8") as file_pointer:
        line = " ".join(str(number) for number in numbers)
        if line:
            file_pointer.write(f"{line}")
        else:
            file_pointer.write("-1")
    print(f"Ghi ket qua thanh cong vao file {filename}")


def main():
    """
    Main function
    """
    numbers = doc_file("data/socp.inp")
    square_numbers = tim_day_so_cp(numbers)
    ghi_file(square_numbers, "data/socp.out")


if __name__ == "__main__":
    main()
