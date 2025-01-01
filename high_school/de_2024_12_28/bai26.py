# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-01 13:56:54
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-01 16:48:18

"""
Bài 26

Tìm dãy con bằng nhau liên tiếp dài nhất trong một dãy số.
Yêu cầu: liệt kê các phần tử của dãy con bằng nhau.

Ví dụ:
maxbn.inp
10
2 2 1 1 1 1 3 4 4 4
maxbn.out
4
1 1 1 1
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
    Returns the sequence of subsequences whose consecutive elements are equal
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


def tim_day_con_dai_nhat(sequence: List[List[int]]) -> List[int]:
    """
    Returns the longest subsequence from the given sequence
    """
    # get the longest length
    longest_length = 0
    for subsequence in sequence:
        longest_length = max(longest_length, len(subsequence))

    # get the longest subsequence
    for subsequence in sequence:
        if len(subsequence) == longest_length:
            return subsequence
    return []


def ghi_file(numbers: List[int], filename: str):
    """
    Writes the length and elements of the given list to file
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
    numbers = doc_file("data/maxbn.inp")
    sequence = tim_day_con_bang_nhau(numbers)
    longest_subsequence = tim_day_con_dai_nhat(sequence)
    ghi_file(longest_subsequence, "data/maxbn.out")


if __name__ == "__main__":
    main()
