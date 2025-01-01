# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-01 06:51:06
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-01 07:05:32

"""
Bài 19

Xoá các phần tử giống nhau trong dãy số, chỉ giữ lại những phần tử đại diện mỗi số.
Sau khi xoá, đưa dãy số ra màn hình.

Ví dụ:
xoatrung.inp
6
3 6 5 3 7 3
xoatrung.out
3 6 5 7
"""
from typing import List


def doc_file(filename: str) -> List[int]:
    """
    Returns the list of numbers read from the second line of given file
    """
    print(f"Doc file {filename}.")
    with open(filename, encoding="utf-8") as file_pointer:
        for i, line in enumerate(file_pointer):
            if i != 1:  # read only the second line
                continue
            numbers = list(map(int, line.split()))
            return numbers


def xoa_trung(numbers: List[int]) -> List[int]:
    """
    Returns the list of unique numbers in the given list
    """
    unique_numbers = []
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)
    return unique_numbers


def ghi_file(numbers: List[int], filename: str):
    """
    Writes the given list of numbers into the given file
    """
    line = " ".join(str(number) for number in numbers)
    with open(filename, "w", encoding="utf-8") as file_pointer:
        file_pointer.write(line)
    print(f"Day so duoc ghi vao file {filename}")


def main():
    """
    Main function
    """
    numbers = doc_file("data/xoatrung.inp")
    unique_numbers = xoa_trung(numbers)
    ghi_file(unique_numbers, "data/xoatrung.out")


if __name__ == "__main__":
    main()
