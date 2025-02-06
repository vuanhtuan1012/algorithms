# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-02-07 05:59:15
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-02-07 06:27:46
"""
Chia mảng

Cho dãy số nguyên không âm a1, a2..., an với 1 <= n <= 1000.
Hãy lập trình tìm cách chia dãy số trên thành 2 đoạn a[1..i] và a[i+1..n]
sao cho tổng các phần tử trong mỗi đoạn bằng nhau (1 <= i < n).

Dữ liệu:
- Dòng 1: chứa số nguyên dương n
- Dòng 2: chứa n số nguyên không âm a1, a2..., an.

Kết quả: ghi ra chỉ số i tìm được. Nếu không có kết quả thì ghi ra số 0

Ví dụ:
- File input: chiamang.inp
5
2 2 3 6 1
- File output: chiamang.out
3
"""

from typing import List


def doc_file(filename: str) -> List[int]:
    """
    Returns list of numbers get from the second line of the given file
    """
    print(f"Read file {filename}")
    day_so = []
    with open(filename, encoding="utf-8") as file_pointer:
        for i, line in enumerate(file_pointer):
            if i != 1:
                continue
            day_so = list(map(int, line.split()))
    return day_so


def tim_index(day_so: List[int]) -> int:
    """
    Returns the index (1-index) in the given list which divide the given sequence
    into two segments so that the sum of the elements in each segment is equal.
    """
    tong = sum(day_so)
    if tong % 2 == 1:
        return 0

    tong //= 2
    i = 0
    while sum(day_so[:i]) < tong:
        i += 1
    if sum(day_so[:i]) == tong:
        return i
    return 0


def ghi_file(filename: str, number: int):
    """
    Write number into file
    """
    with open(filename, "w", encoding="utf-8") as file_pointer:
        file_pointer.write(str(number))
    print(f"Data is written to file {filename}")


def main():
    """
    Main function
    """
    day_so = doc_file("data/chiamang.inp")
    chi_so = tim_index(day_so)
    ghi_file("data/chiamang.out", chi_so)


if __name__ == "__main__":
    main()
