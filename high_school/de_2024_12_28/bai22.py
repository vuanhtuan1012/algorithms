# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-01 09:34:08
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-01 11:13:52

"""
Bài 22

Đảo ngược dãy số. Đưa dãy số đảo ngược ra màn hình.

Ví dụ:
daods.inp
6
3 5 3 6 5 7
daods.out
6
7 5 6 3 5 3
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


def dao_nguoc_day_so(numbers: List[int]) -> List[int]:
    """
    Returns the reverse of the given list
    """
    reversed_numbers = []
    for i in range(len(numbers) - 1, -1, -1):
        reversed_numbers.append(numbers[i])
    return reversed_numbers


def ghi_file(numbers: List[int], filename: str):
    """
    Writes length and the given list to file
    """
    with open(filename, "w", encoding="utf-8") as file_pointer:
        file_pointer.write(f"{len(numbers)}\n")
        line = " ".join(str(number) for number in numbers)
        file_pointer.write(f"{line}\n")
    print(f"Ghi ket qua thanh cong vao file {filename}")


def main():
    """
    Main function
    """
    numbers = doc_file("data/daods.inp")
    reversed_numbers = dao_nguoc_day_so(numbers)
    ghi_file(reversed_numbers, "data/daods.out")


if __name__ == "__main__":
    main()
