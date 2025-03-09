# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-03-09 07:44:28
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-03-09 10:08:36

"""
Bài 3. Lì xì đầu năm
"""
from typing import Tuple


def doc_file(filename: str) -> Tuple[int, int]:
    """
    Returns hai số may mắn n và k
    """
    print(f"Read file: {filename}")
    lucky_numbers = []
    with open(filename, encoding="utf-8") as file_pointer:
        for i, line in enumerate(file_pointer):
            if i >= 2:
                continue
            lucky_numbers.append(int(line.strip()))
    return tuple(lucky_numbers)


def tim_li_xi(lucky_numbers: Tuple[int, int]) -> int:
    """
    Returns số tiền lì xì
    """
    n = str(lucky_numbers[0])
    k = lucky_numbers[1]
    stack = []
    for digit in n:
        while k > 0 and stack and stack[-1] < digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    if k > 0:
        stack = stack[:-k]
    return int("".join(stack)) if stack else -1


def ghi_file(filename: str, li_xi: int):
    """
    Writes số tiền lì xì vào file
    """
    with open(filename, "w", encoding="utf-8") as file_pointer:
        file_pointer.write(str(li_xi))
    print(f"Write to file: {filename}")


def main():
    """
    Main function
    """
    lucky_numbers = doc_file("data/lixi.inp")
    li_xi = tim_li_xi(lucky_numbers)
    ghi_file("data/lixi.out", li_xi)


if __name__ == "__main__":
    main()
