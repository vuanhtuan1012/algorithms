# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-01 11:16:41
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-01 12:34:15

"""
Bài 23

Tìm dãy con liên tiếp không giảm dài nhất của một dãy số.
Yêu cầu: in ra số phần tử và dãy con liên tiếp dài nhất.

Ví dụ:
daykt.inp
6
3 2 5 7 4 6
daykt.out
3
2 5 7
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


def tim_day_con_khong_giam(numbers: List[int]) -> List[List[int]]:
    """
    Returns the sequence of non-decreasing subsequences of the given list of numbers
    """
    sequences = []
    subsequence = []
    for i in range(len(numbers) - 1):
        subsequence.append(numbers[i])
        if numbers[i] > numbers[i + 1]:
            sequences.append(subsequence)
            subsequence = []
    subsequence.append(numbers[-1])
    sequences.append(subsequence)
    return sequences


def tim_day_con_dai_nhat(sequences: List[List[int]]) -> List[int]:
    """
    Returns the longest subsequence from the given list of sequences
    """
    # get the max length
    max_length = 0
    for sequence in sequences:
        max_length = max(max_length, len(sequence))

    # get the longest subsequence
    for subsequence in sequences:
        if len(subsequence) == max_length:
            return subsequence
    return []


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
    numbers = doc_file("data/daykt.inp")
    sequence = tim_day_con_khong_giam(numbers)
    longest_subsequence = tim_day_con_dai_nhat(sequence)
    ghi_file(longest_subsequence, "data/daykt.out")


if __name__ == "__main__":
    main()
