# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2024-12-30 19:31:26
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2024-12-30 22:49:51

"""
Bài 14

Tìm số cặp (i, j) sao cho a_i + a_j = k. Nếu không có ghi ra -1.

Ví dụ:
n = 6, k = 4
dãy số: 1 3 4 2 7 3
kết quả: 2

search.inp
6 4
3 5 9 4 6 2

search.out
-1
"""
from typing import List, Tuple


def doc_file(filename: str) -> Tuple[int, List[int]]:
    """
    Returns the total and the list of numbers read from the given file
    """
    total, numbers = -1, []
    print(f"Doc file {filename}.")
    with open(filename, encoding="utf-8") as file_pointer:
        for i, line in enumerate(file_pointer):
            if i == 0:
                _, total = map(int, line.split())
            if i == 1:
                numbers = list(map(int, line.split()))
    return total, numbers


def tim_cap_chi_so(total: int, numbers: List[int]) -> List[Tuple[int, int]]:
    """
    Returns index pairs of numbers in the list whose sum is the given total
    """
    index_map = {}
    index_pairs = []
    for i, number in enumerate(numbers):
        complement = total - number
        if complement in index_map:
            index_pairs.append((index_map[complement], i))
        index_map[number] = i
    return index_pairs


def ghi_file(index_pairs: List[Tuple[int, int]], filename: str):
    """
    Writes number of index pairs found to the given file
    """
    with open(filename, "w", encoding="utf-8") as file_pointer:
        if index_pairs:
            file_pointer.write(f"{len(index_pairs)}")
        else:
            file_pointer.write("-1")
    print(f"Da ghi so cap chi so tim duoc vao file {filename}")


def main():
    """
    Main function
    """
    total, numbers = doc_file("data/search_bai14.inp")
    index_pairs = tim_cap_chi_so(total, numbers)
    ghi_file(index_pairs, "data/search_bai14.out")


if __name__ == "__main__":
    main()
