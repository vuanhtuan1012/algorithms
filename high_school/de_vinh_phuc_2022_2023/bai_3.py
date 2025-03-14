# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-03-13 14:48:08
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-03-14 14:48:52

"""
Bài 3. Xếp tam giác
"""
from typing import List


def doc_file(filename: str) -> List[int]:
    """
    Returns list of integer numbers get from file
    """
    print(f"Read file: {filename}")
    ds_canh = []
    with open(filename, encoding="utf-8") as file_pointer:
        for i, line in enumerate(file_pointer):
            if i == 0:
                continue
            ds_canh = list(map(int, line.split()))
    return ds_canh


def ghi_file(filename: str, so_tam_giac: int):
    """
    Writes the number of triangles into file
    """
    with open(filename, "w", encoding="utf-8") as file_pointer:
        file_pointer.write(str(so_tam_giac))
    print(f"Write to file: {filename}")


def la_tam_giac(a: int, b: int, c: int) -> bool:
    """
    Returns True if given numbers are sides of a triangle
    Otherwise, False
    """
    if (a + b > c) and (b + c > a) and (c + a > b):
        return True
    return False


def dem_tam_giac(ds_canh: List[int]) -> int:
    """
    Returns the number of unique triangles created by given numbers
    """
    so_tam_giac = 0
    ds_tam_giac = []
    n = len(ds_canh)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                a, b, c = ds_canh[i], ds_canh[j], ds_canh[k]
                if la_tam_giac(a, b, c) and (a, b, c) not in ds_tam_giac:
                    so_tam_giac += 1
                    ds_tam_giac.append((a, b, c))
    return so_tam_giac


def main():
    """
    Main function
    """
    ds_canh = doc_file("data/triangles.inp")
    so_tam_giac = dem_tam_giac(ds_canh)
    ghi_file("data/triangles.out", so_tam_giac)


if __name__ == "__main__":
    main()
