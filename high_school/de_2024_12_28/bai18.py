# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2024-12-30 23:09:04
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2024-12-30 23:19:15

"""
Bài 18

Xoá phần tử tất cả các phần tử chia hết cho k của mảng a có n phần tử.
Đưa ra số phần tử còn lại và mảng a sau khi xoá.

Ví dụ:
modarr.inp
6 2
3 6 5 4 7 2
modarr.out
3
3 5 7
"""
from typing import List, Tuple


def doc_file(filename: str) -> Tuple[int, List[int]]:
    """
    Returns the divisor and the list of numbers read from the given file
    """
    divisor, numbers = 0, []
    print(f"Doc file {filename}.")
    with open(filename, encoding="utf-8") as file_pointer:
        for i, line in enumerate(file_pointer):
            if i == 0:
                _, divisor = map(int, line.split())
            if i == 1:
                numbers = list(map(int, line.split()))
    return divisor, numbers


def xoa_phan_tu(divisor: int, numbers: List[int]) -> List[int]:
    """
    Remove the element divisible by the given number in the given list
    """
    if divisor == 0:
        return numbers

    numbers_cleaned = []
    for number in numbers:
        if number % divisor != 0:
            numbers_cleaned.append(number)
    return numbers_cleaned


def ghi_file(numbers: List[int], filename: str):
    """
    Writes length and numbers of the given list to file
    """
    with open(filename, "w", encoding="utf-8") as file_pointer:
        file_pointer.write(f"{len(numbers)}\n")
        line = " ".join(str(num) for num in numbers)
        file_pointer.write(f"{line}\n")
    print(f"Ghi ket qua thanh cong vao file {filename}")


def main():
    """
    Main function
    """
    divisor, numbers = doc_file("data/modarr.inp")
    numbers = xoa_phan_tu(divisor, numbers)
    ghi_file(numbers, "data/modarr.out")


if __name__ == "__main__":
    main()
