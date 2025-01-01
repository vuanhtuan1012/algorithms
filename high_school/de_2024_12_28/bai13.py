# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2024-12-29 10:17:08
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-01 11:12:28

"""
Bài 13

Liệt kê các dãy con liên tiếp không giảm (có nhiều hơn 1 phần tử) của dãy ban đầu,
mỗi dãy trên một dòng.

Ví dụ:
search.inp
6
3 4 6 2 7 3
search.out
3 4 6
2 7
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


def tim_cac_chuoi_con(numbers: List[int]) -> List[List[int]]:
    """
    Returns the list of subsequences with at least 2 elements
    and non-decreasing consecutive elements
    """
    subsequences = []
    subsequence = []
    for i in range(len(numbers) - 1):
        subsequence.append(numbers[i])
        if numbers[i] > numbers[i + 1]:
            if len(subsequence) > 1:
                subsequences.append(subsequence)
            subsequence = []
    if len(subsequence) > 1:
        subsequences.append(subsequence)
    return subsequences


def ghi_file(subsequences: List[List[int]], filename: str):
    """
    Writes subsequences into the given file, each subsequence in a line
    """
    with open(filename, "w", encoding="utf-8") as file_pointer:
        for subsequence in subsequences:
            line = " ".join(str(element) for element in subsequence)
            file_pointer.write(f"{line}\n")
    print(f"Cac chuoi con duoc ghi vao file {filename}")


def main():
    """
    Main function
    """
    numbers = doc_file("data/search.inp")
    subsequences = tim_cac_chuoi_con(numbers)
    ghi_file(subsequences, "data/search.out")


if __name__ == "__main__":
    main()
