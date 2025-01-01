# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-01 13:33:42
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-01 13:50:05

"""
Bài 25

Tìm dãy con bằng nhau liên tiếp trong một dãy số.
Yêu cầu: liệt kê các phần tử của dãy con bằng nhau.

Ví dụ:
bangnhau.inp
6
2 2 2 7 4 4
bangnhau.out
2 2 2
4 4
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


def tim_day_con_bang_nhau(numbers: List[int]) -> List[List[int]]:
    """
    Returns the sequence of subsequences with equal elements
    """
    sequence = []
    subsequence = []
    for i in range(len(numbers) - 1):
        subsequence.append(numbers[i])
        if numbers[i] != numbers[i + 1]:
            if len(subsequence) > 1:
                sequence.append(subsequence)
            subsequence = []
    subsequence.append(numbers[-1])
    if len(subsequence) > 1:
        sequence.append(subsequence)
    return sequence


def ghi_file(sequence: List[List[int]], filename: str):
    """
    Writes subsequences of the given sequence to file
    """
    with open(filename, "w", encoding="utf-8") as file_pointer:
        for subsequence in sequence:
            line = " ".join(str(number) for number in subsequence)
            file_pointer.write(f"{line}\n")
    print(f"Ghi ket qua thanh cong vao file {filename}")


def main():
    """
    Main function
    """
    numbers = doc_file("data/bangnhau.inp")
    sequence = tim_day_con_bang_nhau(numbers)
    ghi_file(sequence, "data/bangnhau.out")


if __name__ == "__main__":
    main()
