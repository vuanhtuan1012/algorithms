# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-03-03 22:37:02
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-03-03 23:53:05

"""
Bài 2. Số đẹp
"""
from typing import List


def read_file(filename: str) -> List[int]:
    """
    Returns list of numbers from the given file
    """
    print(f"Read file {filename}")
    numbers = []
    with open(filename, encoding="utf-8") as file_pointer:
        for i, line in enumerate(file_pointer, start=1):
            # skip the first line
            if i == 1:
                continue
            numbers = list(map(int, line.strip().split()))
    return numbers


def write_file(filename: str, numbers: List[int]):
    """
    Writes numbers into file
    """
    with open(filename, "w", encoding="utf-8") as file_pointer:
        file_pointer.write("\n".join(map(str, numbers)))
    print(f"Numbers are written to file {filename}")


def is_prime(number: int) -> bool:
    """
    Returns True if the given number is prime, otherwise False
    """
    # pre-check condition
    if number < 2:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def is_beautiful(number: int) -> bool:
    """
    Returns True if the given number is beautiful, otherwise False
    """
    while number // 10 > 0:
        if not is_prime(number):
            return False
        number = number // 10
    return is_prime(number)


def main():
    """
    Main function
    """
    numbers = read_file("data/sodep.inp")
    beautiful_numbers = [num for num in numbers if is_beautiful(num)]
    write_file("data/sodep.out", beautiful_numbers)


if __name__ == "__main__":
    main()
