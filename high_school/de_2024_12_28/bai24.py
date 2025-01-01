# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-01 12:35:12
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-01 12:42:18

"""
Bài 24

Tìm dãy con liên tiếp không giảm có tổng lớn nhất.
Kết quả ghi ra tổng và liệt kê các phần tử có tổng lớn nhất.

Ví dụ:
daykt.inp
6
3 2 5 7 4 6
daykt.out
14
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


def tim_day_con_tong_lon_nhat(sequences: List[List[int]]) -> List[int]:
    """
    Returns the subsequence with the largest sum
    """
    # get the largest sum
    largest_sum = 0
    for sequence in sequences:
        largest_sum = max(largest_sum, sum(sequence))

    # get the subsequence with the largest sum
    for subsequence in sequences:
        if sum(subsequence) == largest_sum:
            return subsequence
    return []


def ghi_file(numbers: List[int], filename: str):
    """
    Writes the sum and the numbers of given list to file
    """
    with open(filename, "w", encoding="utf-8") as file_pointer:
        file_pointer.write(f"{sum(numbers)}\n")
        line = " ".join(str(number) for number in numbers)
        file_pointer.write(f"{line}\n")
    print(f"Ghi ket qua thanh cong vao file {filename}")


def main():
    """
    Main function
    """
    numbers = doc_file("data/daykt.inp")
    sequence = tim_day_con_khong_giam(numbers)
    subsequence = tim_day_con_tong_lon_nhat(sequence)
    ghi_file(subsequence, "data/daykt_bai24.out")


if __name__ == "__main__":
    main()
